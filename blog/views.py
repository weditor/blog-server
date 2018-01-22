from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets, generics, mixins
from .models import Article, Tag, Reply
from .serializers import ArticleSerializer, ReplySerializer, TagSerializer
# from mylibs.view_mixins import PrivateQueryMixin
# from mylib.filters import CommonFilter
# Create your views here.


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_fields = ['title', 'title__icontains']

    def get_queryset(self):
        queryset = super(ArticleViewset, self).get_queryset()
        print (self.request.user)
        if not self.request.user or not self.request.user.is_authenticated:
            queryset = queryset.filter(is_private=False).exclude(tags__in=Tag.objects.filter(is_private=True))
        return queryset


class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_fields = ['name__icontains']

    def get_queryset(self):
        queryset = super(TagViewset, self).get_queryset()
        word = self.request.query_params.get('search')
        if word:
            queryset = queryset.filter(Q(name__icontains=word) | Q(pinyin__icontains=word))
        return queryset

    def destroy(self, request, *args, **kwargs):
        raise NotImplementedError('not implement')


class ReplyViewset(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    def destroy(self, request, *args, **kwargs):
        raise NotImplementedError('not implement')
