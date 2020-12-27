from django.urls import path
from . import views
urlpatterns = [
   path('', views.ListSkill.as_view(), name=views.ListSkill.name),
   path('<uuid:pk>', views.DetailSkill.as_view(), name=views.DetailSkill.name),

]