from django.shortcuts import render

from rest_framework import generics

from .models import Article, Category  # Tags
from .serializers import ArticleSerializer, CategorySerializer  # TagsSerializer


# Create your views here.

#
# class ListTags(generics.ListCreateAPIView):
#     queryset = Tags.objects.all()
#     serializer_class = TagsSerializer
#     name = 'tags_list'
#
#
# class DetailTags(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tags.objects.all()
#     serializer_class = TagsSerializer
#     name = 'tags_detail'


class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category_list'


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category_detail'


class ListArticle(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    name = 'article_list'


class DetailArticle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    name = 'article_detail'
