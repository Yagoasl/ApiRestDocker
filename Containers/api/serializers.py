from rest_framework import serializers
from Containers import models

class dockerfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.dockerfile
        fields = '__all__'


class dockerComposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.dockerCompose
        fields = '__all__'
