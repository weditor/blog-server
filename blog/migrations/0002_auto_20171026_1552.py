# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='quote',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Reply', verbose_name='引用'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='synonym',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Tag', verbose_name='关联标签'),
        ),
    ]
