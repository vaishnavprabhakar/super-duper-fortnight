from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"




