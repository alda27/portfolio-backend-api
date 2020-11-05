from django.urls import path
from . import views
urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('contact', views.contact, name='contact'),
]