from django.shortcuts import render
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.viewsets import mixins
from django.http import JsonResponse
# Create your views here.


# class UserViewset(mixins.ListModelMixin, GenericViewSet)

def GetUser(request):
    return JsonResponse(UserSerializer(request.user).data)






