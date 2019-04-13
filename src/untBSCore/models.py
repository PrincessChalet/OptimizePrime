from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class UNTBSCore(models.Model):
    category = models.CharField(max_length=50)
    hours = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.category