from django.db import models
from rest_framework import serializers

from user.models import User
# Create your models here.

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        extra_kwargs = {
            'password': {'write_only': True},
        }

        fields = (
            'id',
            'name',
            'username',
            'password'
        )