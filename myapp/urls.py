from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('network/list/',views.networklist,name='networklist'),
    #path('network/containers/',views.networkcontainers,name='networkcontainers'),
    path('network/create/',views.networkcreate,name='networkcreate'),
    path('network/remove/',views.networkremove,name='networkremove'),
    path('image/remove/',views.removeimage,name="imageremove"),
    path('image/build/',views.buildimage,name="imagebuild"),
    path('image/pull/',views.pullimage,name="imagepull"),
    path('image/show/',views.showimages,name="imageshow"),
    path('container/run/',views.runcontainer,name='containerrun'),
    #path('container/exec/',views.execcontainer,name='containerexec'),
    path('container/kill/',views.killcontainer,name='containerkill'),
    path('container/logs/',views.logscontainer,name='containerlogs'),
    path('container/remove/',views.removecontainer,name='containerremove'),
    path('container/rename/',views.renamecontainer,name='containerrename'),
    path('container/start/',views.startcontainer,name='containerstart'),
    path('container/stop/',views.stopcontainer,name='containerstop'),
    path('container/show/',views.showcontainer,name='containershow'),
    
]