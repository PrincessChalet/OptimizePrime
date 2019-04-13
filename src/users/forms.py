from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Student

class StudentCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Student
        fields = ('username', 'email')

class StudentChangeForm(UserChangeForm):

    class Meta:
        model = Student
        fields = ('username', 'email')