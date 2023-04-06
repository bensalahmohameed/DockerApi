from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from requests import request



def index(request):

    return render (request,'index.html')

def runcontainer(request):
#detach: run command in detached mode
#cpu_percent : percentage of usage cpu
#network : network (str) – Name of the network this container will be connected to at creation time
#ports (dict): The port number, as an integer. For example, {'2222/tcp': 3333} will expose port 2222 inside the container as port 3333 on the host.
#network_mode (str) – One of:

    #bridge Create a new network stack for the container on on the bridge network.
    #none No networking for this container.
    #container:<name|id> Reuse another container’s network stack.
    #host Use the host network stack. This mode is incompatible with ports.

#name: give a name to the container
#environment (dict or list) – Environment variables to set inside the container, as a dictionary or a list of strings in the format ["SOMEVARIABLE=xxx"].







#id  The ID of the object.

#image    The image of the container.

#labels    The labels of a container as dictionary.

#name    The name of the container.

#short_id    The ID of the object, truncated to 10 characters.

#status    The status of the container. For example, running, or exited. The raw representation of this object from the server.






    if request.method == 'POST':
        import docker
        client=docker.from_env()
        imagename=request.POST['imagename']
        hostport=int(request.POST['hostport']) 
        #tcp, udp, or sctp. 
        containerport=request.POST['containerport'] 
        porttype=request.POST['radio'] 
        
        contport=containerport+'/'+porttype 
        #cpu_percente=int(request.POST['cpu'])
        networke=request.POST['network']
        namee=request.POST['name']
        
    
        container = client.containers.run(image=imagename,ports={contport: hostport},detach=True,name=namee)#cpu_percent=cpu_percente,) 
        return render(request,'runnedcontainer.html',{'container':container})

    else:
        return render(request,'runcontainer.html')
    
   


    

#def execcontainer(request):

    #Similar to docker exec
   #if request.method == 'POST' :
#

   #     import docker
   #     client = docker.from_env()
   #     containername=request.POST["containername"]
   #     container = client.containers.get(containername)
   #     container.exec_run(container)
   #     return render(request,'excexedcontainer.html')
   # else :

   #     


def killcontainer(request):
    #similar to docker kill
    if request.method == 'POST':
        import docker
        client=docker.from_env()
        containername=request.POST['containername']
        container=client.containers.get(containername)
        container.kill()
        return render(request,'killedcontainer.html',{'container':container})

    else:
        return render(request,'killcontainer.html')

def logscontainer(request):
    # similar to docker logs
    
    if request.method == 'POST':
        import docker
        client=docker.from_env()
        containername=request.POST['containername']
        container=client.containers.get(containername)
        return render(request,'loggedcontainer.html',{'container':container.logs()})

    else:
        return render(request,'logcontainer.html')

def removecontainer(request):
    # similar to docker rm    
    if request.method == 'POST':
        import docker
        client=docker.from_env()
        containername=request.POST['containername']
        container=client.containers.get(containername)
        container.remove(force=True)
        return render(request,'removedcontainer.html',{'container':container})

    else:
        return render(request,'removecontainer.html')

def renamecontainer(request):
    # similar to docker rename
    if request.method == 'POST':
        import docker
        client=docker.from_env()
        containername=request.POST['containername']
        container=client.containers.get(containername)
        newname=request.POST['newname']
        container.rename(newname)
        containerr=client.containers.get(containername)
        return render(request,'renamedcontainer.html',{'containerr':containerr,'container':container})

    else:
        return render(request,'renamecontainer.html')
    

def startcontainer(request):
    # similar to docker start
    if request.method == 'POST':
        import docker
        client=docker.from_env()
        containername=request.POST['containername']
        container=client.containers.get(containername)
        container.start()
        return render(request,'startedcontainer.html',{'container':container})

    else:
        return render(request,'startcontainer.html')
    

def showcontainer (request):
#docker ps -a

#all: docker ps -a

    import docker
    client = docker.from_env()
    containers=client.containers.list(all)
    return render(request,'showcontainer.html',{'containers':containers})

def stopcontainer(request):

    # similar to docker stop
    if request.method == 'POST':
        import docker
        client=docker.from_env()
        containername=request.POST['containername']
        container=client.containers.get(containername)
        container.stop()
        return render(request,'stoppedcontainer.html',{'container':container})

    else:
        return render(request,'stopcontainer.html')
    
        








#--------------------------------------------------------------------------------------------------------------------------------
#attrs

    #The raw representation of this object from the server.

#id

    #The ID of the object.

#labels

    #The labels of an image as dictionary.

#short_id

    #the ID of the image truncated to 10 characters, plus the sha256: prefix.

#ags

    #The image’s tags.




def showimages(request):

    liist=[]
    import docker
    client = docker.from_env()
    for image in client.images.list():
        liist.append(image.attrs['RepoTags'])



    return render (request,'showimages.html',{'liist':liist})
        

def pullimage(request):
    if request.method == 'POST' :
        # lezem nekhdem if image already pulled
        imagename=request.POST["imagename"]
        import docker
        client = docker.from_env()
        image = client.images.pull(imagename)

        return render(request,'pulledimage.html',{'image.short_id':image.short_id})
    else :
        return render(request,'pullimage.html')

def buildimage(request):
    #path (str) – Path to the directory containing the Dockerfile
    #tag (str) – A tag to add to the final image
    if request.method == 'POST' :
        imagepath=request.POST["imagepath"]
        imagetag=request.POST["imagetag"]
        import docker
        client = docker.from_env()
        image = client.images.build(path=imagepath,tag=imagetag)

        return render(request,'builtimage.html',{'image':image})

    else :
        return render(request,'buildimage.html')

def removeimage(request):
    ### mazel if image do not exist
    ### mazel ki mayforcich w tetfasakhch
    #similar to docker rmi
    #Parameters:	
        #image (str) – The image to remove
        #force (bool) – Force removal of the image
    if request.method == 'POST' :    
        imageid=request.POST["imageid"]
        radio=request.POST["radio"]
        import docker
        client=docker.from_env()
        if radio=="True":
            radio=True
        else:
            radio=False
        image = client.images.remove(image=imageid,force=radio)
    
        return render(request,'removedimage.html',{'image':image})
    
    else :
        return render(request,'removeimage.html')




#-------------------------------------------------------------------------------------------------------------------------------------------


#id

    #The ID of the object.

#short_id

    #The ID of the object, truncated to 10 characters.

#name

    #The name of the network.

#containers

    #The containers that are connected to the network, as a list of Container objects.

#attrs

    #The raw representation of this object from the server.


#@api_view(['GET'])
def networklist(request):
    listname=[]
    import docker
    client = docker.from_env()
    networks=client.networks.list()
    for network in networks:
        listname.append((network.name,network.short_id))
        
    return render (request,'networklist.html',{'listname':listname})



def networkcreate(request):
#name (str) – Name of the network
    if request.method=="POST":
        networkname=request.POST["networkname"]
        import docker
        client = docker.from_env()
        network=client.networks.create(name=networkname)

        return render(request,'creatednetwork.html',{'network':network})
    else:
        return render (request,'createnetwork.html')

def networkremove(request):
    if request.method=="POST":
        networkid=request.POST["networkid"]
        import docker
        client=docker.from_env()
        ttw=client.networks.get(networkid)
        ttw.remove()
        
        return render(request,'removednetwork.html',{'ttw':ttw})
    
    else :
        return render(request,'removenetwork.html')
#def networkcontainers(request):
   # if request.method=="POST":
    #    networkid=request.POST["networkid"]
    #    lista=[]
    #    import docker
      #  client=docker.from_env()
      #  for container in client.networks.get(networkid).containers():
       #     lista.append[container.name]
        
        #return render(request,'containersnetwork.html',{'lista':lista})
    
    #else :
        #return render(request,'containernetwork.html')








