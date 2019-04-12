from django import forms
from .models import Degree


#### may need to change this later to a typed choice field
class DegreeSelectionForm(forms.Form):
    degreeList = Degree.objects.all()
    
    degrees = []

    #print(degreeList)
    for degree in degreeList:
        degrees.append((degree.name,  degree.name))

    #print(degrees)# just a test print

    degreeChoices = forms.ChoiceField(choices=degrees)

class CoursesSelectionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        print(kwargs.pop('test'))

    tempArr = []
    degreeRequirements = {
                "Computer Science and Engineering": [
                    "CSCE 1030",
                    "CSCE 1040",
                    "CSCE 2100",
                    "CSCE 2110",
                    "CSCE 2610",
                    "CSCE 3110",
                    "CSCE 3600",
                    "CSCE 4010",
                    "CSCE 4110",
                    "CSCE 4444",
                    [
                        "CSCE 4901",
                        "CSCE 4999"
                    ]
                ]
    }\


    #this makes a list from all of the entries form the database
    for category in degreeRequirements:
        for course in degreeRequirements[category]:
            if type(course) is str:
                temp = (course, course)
                tempArr.append(temp)
            elif type(course) == list :
                tempStr = ''
                for subcourse in course:
                    tempStr = tempStr + ' or ' + subcourse
                temp = (tempStr, tempStr)
                tempArr.append(temp)

    #Here the array ^ becaomes the checkbox choices 
    checks = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=tempArr
    )

#class CourseCheckbox(forms.Form):