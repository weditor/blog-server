from django.shortcuts import render
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.viewsets import mixins
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# class UserViewset(mixins.ListModelMixin, GenericViewSet)

def GetUser(request):
    return JsonResponse(UserSerializer(request.user).data)


@csrf_exempt
def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(username, password)
    user = authenticate(username=username, password=password)
    print('user is', user)
    if user is None:
        return JsonResponse(UserSerializer(None).data)
    login(request, user)
    return JsonResponse(UserSerializer(user).data)


def logout_view(request):
    if request.user is None:
        return JsonResponse({'status': 0, "message": 'ok'})
    logout(request)
    return JsonResponse({'status': 0, "message": 'ok'})
