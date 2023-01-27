from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    username = models.CharField(max_length=50, blank=False, null=False, unique=True)
    password = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        db_table = 'user'