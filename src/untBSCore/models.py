from django.db import models

# Create your models here.
class UNTBSCore(models.Model):
    category = models.CharField(max_length=50)
    hours = models.PositiveSmallIntegerField()