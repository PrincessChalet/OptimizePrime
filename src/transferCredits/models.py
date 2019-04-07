from django.db import models

# Create your models here.
class TransferCredit(models.Model):
    courseID = models.PositiveSmallIntegerField(null=True, blank=True)
    courseDept = models.CharField(max_length=4,null=True, blank=True)
    name = models.CharField(max_length=50)
    equivalentToID = models.CharField(max_length=4)
    equivalentToDept = models.CharField(max_length=4)
    requiredScore = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return self.name