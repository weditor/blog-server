from rest_framework import serializers
from .models import Article, Tag, Reply


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'create_time', 'change_time']

