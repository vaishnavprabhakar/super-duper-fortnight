from rest_framework import viewsets

from django.contrib.auth import get_user_model

from .serializer import UserSerializer

from rest_framework.permissions import IsAuthenticated


from rest_framework.views import APIView
# Create your views here.


