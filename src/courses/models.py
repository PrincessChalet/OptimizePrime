from django.db import models

# Create your models here.

class Course(models.Model):
    FALL = 'Fall'
    SPRING = 'Spring'
    BOTH = 'Both'

    SEMESTER_CHOICES = ((FALL, 'Fall'),(SPRING,'Spring'),(BOTH, 'Both'))

    courseID = models.PositiveSmallIntegerField()
    courseDept = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    prereqCount = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=50)
    hours = models.PositiveSmallIntegerField()
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES, default=BOTH)
    description = models.TextField()

    def __str__(self):
        return self.name

class Prereq(models.Model):
    courseID = models.PositiveSmallIntegerField()
    courseDept = models.CharField(max_length=4)
    name = models.CharField(max_length=100, default='prereq course name')
    prereqCourseID = models.PositiveSmallIntegerField()
    prereqCourseDept = models.CharField(max_length=4)

    def __str__(self):
        return self.name