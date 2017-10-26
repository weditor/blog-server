from django.shortcuts import render
from rest_framework import viewsets, generics, mixins
from .models import Article, Tag, Reply
from .serializers import ArticleSerializer, ReplySerializer, TagSerializer
# Create your views here.


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def destroy(self, request, *args, **kwargs):
        raise NotImplementedError('not implement')


class ReplyViewset(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def destroy(self, request, *args, **kwargs):
        raise NotImplementedError('not implement')

