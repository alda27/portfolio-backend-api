from django.urls import path
from . import views
urlpatterns = [
   path('', views.ListArticle.as_view(), name=views.ListArticle.name),
   path('article/<uuid:pk>', views.DetailArticle.as_view(), name=views.DetailArticle.name),
   path('tags/', views.ListTags.as_view(), name=views.ListTags.name),
   path('tags/<uuid:pk>', views.DetailTags.as_view(), name=views.DetailTags.name),
   path('category/', views.ListCategory.as_view(), name=views.ListCategory.name),
   path('category/<uuid:pk>', views.DetailCategory.as_view(), name=views.DetailCategory.name),
]