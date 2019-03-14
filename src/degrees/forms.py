from django import forms
from .models import Degree


#### may need to change this later to a typed choice field
class DegreeSelectionForm(forms.Form):
    degreeList = Degree.objects.all()
    
    degrees = []
    for degree in degreeList:
        degrees.append((degree.name,  degree.name))

    #print(degrees)# just a test print

    degreeChoices = forms.ChoiceField(choices=degrees)
