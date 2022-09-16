from rest_framework import viewsets
from Containers.api import serializers
from Containers import models

class dockerfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.dockerfileSerializer
    queryset = models.dockerfile.objects.all()

class dockerComposeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.dockerComposeSerializer
    queryset = models.dockerCompose.objects.all()