from rest_framework import serializers
from .models import Article, Tag, Reply


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'pinyin', 'description', 'create_time', 'change_time', 'is_private']
        extra_kwargs = {'pinyin': {'read_only': True}}


class ArticleSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        if 'tags' in data:
            data['tags'] = [Tag.objects.get_or_create(name=name)[0].id for name in set(data['tags'])]
        return super(ArticleSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        data = super(ArticleSerializer, self).to_representation(instance)
        data['tags'] = [TagSerializer(tag).data for tag in Tag.objects.filter(id__in=data['tags'])]
        # data['tags'] = [TagSerializer(tag).data for tag in Tag.objects.filter(id__in=data['tags'])]
        return data

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'create_time', 'change_time', 'tags', 'is_private']


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'content', 'create_time']
