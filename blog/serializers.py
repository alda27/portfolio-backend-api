from rest_framework import serializers
from .models import Article, Category  # Tags


# class TagsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tags
#         fields = '__all__'
#

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
