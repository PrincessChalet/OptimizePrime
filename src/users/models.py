from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
 
# Create your models here.
class Student(AbstractUser):

	email = models.CharField(max_length=50)
	password = models.CharField(max_length=128, default='temp')

	USERNAME_FIELD = 'username'

