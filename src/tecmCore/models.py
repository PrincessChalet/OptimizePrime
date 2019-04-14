from django.db import models
from django.contrib.postgres.fields import JSONField
class TechClasses(models.Model):
    name = models.CharField(max_length=50)
    tecmCoreInfo = JSONField()
# Create your models here.
