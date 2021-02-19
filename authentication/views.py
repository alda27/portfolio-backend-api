from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.

# I WONT USE THIS BECAUSE I DONT NEED. IT WAS A TEST
# class LoginUser(APIView):
#     permission_classes = (AllowAny,)
#
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             return Response({'token': user.auth_token.key})
#         else:
#             return Response({'error': 'Wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)

# class LoginUser(ObtainAuthToken):
#    """Handle creating user authenticated tokens"""
#  renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES  # Used for render browsable api
