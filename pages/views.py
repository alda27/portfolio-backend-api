from django.shortcuts import render, HttpResponse
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import generics
from projects import views as project_views
from blog import views as blog_views
from skills import views as skill_views


# Create your views here.

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'projects': reverse(project_views.ListProject.name, request=request),
            'projects-tags': reverse(project_views.ListTags.name, request=request),
            'blog': reverse(blog_views.ListArticle.name, request=request),
            'skills': reverse(skill_views.ListSkill.name, request=request)
        })


def contact(request):
    return HttpResponse('page contact')
