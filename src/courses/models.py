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
        return (self.courseDept + " " + str(self.courseID) + ": " +  self.name)

class Prereq(models.Model):
    courseID = models.PositiveSmallIntegerField()
    courseDept = models.CharField(max_length=4)
    name = models.CharField(max_length=100, default='prereq course name')

    #Note: When filling in the table, we list MATH 1650 as the course and prereq MATH 1710, which makes it look like its saying that MATH 1710 is a prereq for MATH 1650, but we do that because one single course is the prereq to to another but a course may have multiple prereqs.
    prereqCourseID = models.PositiveSmallIntegerField()
    prereqCourseDept = models.CharField(max_length=4)

    def __str__(self):
        return self.courseDept + " " + str(self.courseID) + " -> " + self.prereqCourseDept + " " +  str(self.prereqCourseID)
        