from django.shortcuts import render, HttpResponse
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import generics
from projects import views


# Create your views here.

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'projects': reverse(views.ListProject.name, request=request),
            'projects-tags': reverse(views.ListTags.name, request=request)
        })


def contact(request):
    return HttpResponse('page contact')
