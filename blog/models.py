#coding:utf-8
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

# from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.urls import  reverse

# Create your models here.
#分类
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
#标签
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
#文章
@python_2_unicode_compatible
class Post(models.Model):
    #文章标题
    title = models.CharField(max_length=70)
    #正文
    body = models.TextField()
    #文章的创建时间和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    #摘要，blank=true表示参数可以为空
    excerpt = models.CharField(max_length=200,blank=True)
    #我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，
    # 所以我们使用的是 ForeignKey，即一对多的关联关系。
    category = models.ForeignKey(Category)
    #而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，
    # 所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    tags = models.ManyToManyField(Tag,blank=True)
    #django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，
    # User 是 Django 为我们已经写好的用户模型。
    author = models.ForeignKey(User)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    class Meta:
        #ordering属性用来指定文章排序顺序（按照创建时间的逆序来排序）
        ordering = ['-created_time']