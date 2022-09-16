from django.contrib import admin
from django.urls import path, include

from Containers.views import imagens

from rest_framework import routers
from Containers.api import viewsets as dockerviewsets

route1 = routers.DefaultRouter()
route2 = routers.DefaultRouter()

route1.register(r'dockerfile', dockerviewsets.dockerfileViewSet, basename='Dockerfile')
route2.register(r'dockerCompose', dockerviewsets.dockerComposeViewSet, basename='Docker-Compose')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route1.urls)),
    path('', include(route2.urls)),
    path('imagens/', imagens),
]