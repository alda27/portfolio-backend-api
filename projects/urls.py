from django.urls import path
from . import views
urlpatterns = [
   path('', views.ListProject.as_view(), name='projects'),
   path('<uuid:pk>', views.DetailProject.as_view(), name='project_detail'),
]