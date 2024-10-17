from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json
from .models import Photo
from django.core.files.storage import default_storage
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'User already exists'}, status=400)
        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({'message': 'User registered successfully'}, status=201)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        return JsonResponse({'error': 'Invalid credentials'}, status=400)

def user_logout(request):
    logout(request)
    return JsonResponse({'message': 'Logged out'}, status=200)

@csrf_exempt
@require_http_methods(['POST'])
def upload_photo(request):
    if request.user.is_authenticated:
        image = request.FILES['image']
        photo = Photo(user=request.user, image=image)
        photo.save()
        return JsonResponse({'message': 'Photo uploaded'}, status=201)
    return JsonResponse({'error': 'Unauthorized'}, status=401)

def user_photos(request):
    if request.user.is_authenticated:
        photos = Photo.objects.filter(user=request.user).values('image', 'uploaded_at')
        return JsonResponse(list(photos), safe=False)
    return JsonResponse({'error': 'Unauthorized'}, status=401)
