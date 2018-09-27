from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from mdeditor.fields import MDTextField


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category)
    content = MDTextField(verbose_name='正文')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    summary = models.CharField(max_length=200, verbose_name='概要')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name
