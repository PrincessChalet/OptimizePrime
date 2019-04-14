from django.db import models
from django.contrib.postgres.fields import JSONField

class MathClasses(models.Model):
    name = models.CharField(max_length=50)
    mathCoreInfo = JSONField()
# Create your models here.
