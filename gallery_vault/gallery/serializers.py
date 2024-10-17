from rest_framework import serializers
from .models import Image
from django.contrib.auth.models import User

class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Image
        fields = ['id', 'owner', 'title', 'image_file', 'uploaded_at']

class UserSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'images']