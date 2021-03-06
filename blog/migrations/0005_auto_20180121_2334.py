# Generated by Django 2.0.1 on 2018-01-21 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_tag_pinyin'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ceator',
            field=models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='article',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='私密'),
        ),
        migrations.AddField(
            model_name='reply',
            name='ceator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='tag',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='私密'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='文章标签'),
        ),
    ]
