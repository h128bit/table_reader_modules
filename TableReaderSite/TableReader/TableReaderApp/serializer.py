from rest_framework import serializers
from TableReaderApp.models import *


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()


class TableReaderAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'email', 'subscription_end_date')
