from django.contrib import admin

# Register your models here.
from .models import Course, Prereq

admin.site.register(Course)
admin.site.register(Prereq)