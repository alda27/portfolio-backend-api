"""portfolio_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include('pages.urls')),
                  path('api/v1/projects/', include('projects.urls')),
                  path('api/v1/blog/', include('blog.urls')),
                  path('api/v1/skills/', include('skills.urls')),
                  # path('api/v1/', include('authentication.urls')), # dont use it anymore
                  # path('api-auth/', include('rest_framework.urls')),  # i have to use for based authentication token
                  path('api/v1/rest-auth/', include('rest_auth.urls')),  # third-party package allauth
                  path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),  # third-party
                  # package allauth
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
