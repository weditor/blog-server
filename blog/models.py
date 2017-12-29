from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField('标签', max_length=30)
    synonym = models.ForeignKey('self', verbose_name='关联标签', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.CharField('描述', max_length=100, default="", blank=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    change_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=100)
    content = models.TextField(verbose_name='内容')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    change_time = models.DateTimeField('修改时间', auto_now=True)
    tags = models.ManyToManyField(Tag, verbose_name="文章标签")
    
    def __str__(self):
        return self.title


class Reply(models.Model):
    content = models.CharField('内容', max_length=150)
    article = models.ForeignKey(Article, verbose_name="所属文章", on_delete=models.CASCADE)
    quote = models.ForeignKey('self', verbose_name="引用", null=True, blank=True, on_delete=models.SET_NULL)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
