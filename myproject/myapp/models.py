from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="name")
    description = models.TextField(verbose_name="description")
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name="name")
    description = models.TextField(verbose_name="description")
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="title")
    content = models.TextField(verbose_name="content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

class Comment(models.Model):
    article_id = models.IntegerField()
    user_id = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
