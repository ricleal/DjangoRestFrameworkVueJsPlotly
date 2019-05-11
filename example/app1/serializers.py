from .models import Heart
from rest_framework import serializers


class HeartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Heart
        fields = '__all__'
