from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

class Tags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # I used uuid to make easier the id
    # field
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tags'
        verbose_name_plural = 'Tags'
        ordering = ('-date_created',)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('-date_created',)

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    content_prev = models.CharField(max_length=250)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='articles/%Y/%m/%d/', default='articles/default.jpg')
    tags = models.ManyToManyField(Tags, related_name='articles_tags', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles_author')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='articles_category')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ('-date_created',)

    def __str__(self):
        return self.title
