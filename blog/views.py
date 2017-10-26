from django.shortcuts import render
from rest_framework import viewsets, generics, mixins
from .models import Article, Tag, Reply
from .serializers import ArticleSerializer
# Create your views here.


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
