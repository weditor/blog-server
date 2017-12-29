from django.shortcuts import render
from rest_framework import viewsets, generics, mixins
from .models import Article, Tag, Reply
from .serializers import ArticleSerializer, ReplySerializer, TagSerializer
# from mylib.filters import CommonFilter
# Create your views here.





class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_fields = ['title', 'title__icontains']


class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_fields = ['name__icontains']

    def destroy(self, request, *args, **kwargs):
        raise NotImplementedError('not implement')


class ReplyViewset(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def destroy(self, request, *args, **kwargs):
        raise NotImplementedError('not implement')
