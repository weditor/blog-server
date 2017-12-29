from rest_framework import serializers
from .models import Article, Tag, Reply


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'description', 'create_time', 'change_time']


class ArticleSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        data['tags'] = [Tag.objects.get(name=name).id for name in data['tags']]
        return super(ArticleSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        data = super(ArticleSerializer, self).to_representation(instance)
        data['tags'] = [TagSerializer(tag).data for tag in Tag.objects.filter(id__in=data['tags'])]
        return data

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'create_time', 'change_time', 'tags']


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'content', 'create_time']
