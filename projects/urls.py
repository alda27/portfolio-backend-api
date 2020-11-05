from django.urls import path
from . import views
urlpatterns = [
   path('', views.ListProject.as_view(), name=views.ListProject.name),
   path('<uuid:pk>', views.DetailProject.as_view(), name=views.DetailProject.name),
   path('tags', views.ListTags.as_view(), name=views.ListTags.name),
   path('tags/<uuid:pk>', views.DetailTags.as_view(), name=views.DetailTags.name),
]