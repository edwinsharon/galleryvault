from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Photo
from .serializers import PhotoSerializer

# List all photos of the authenticated user and upload a new photo
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_gallery(request):
    if request.method == 'GET':
        photos = Photo.objects.filter(user=request.user)
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, or delete a specific photo
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk, user=request.user)

    if request.method == 'GET':
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PhotoSerializer(photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from django.http import JsonResponse

def get_token(request):
    # Example token generation logic or response
    token = "your-generated-token-here"
    return JsonResponse({"token": token})
