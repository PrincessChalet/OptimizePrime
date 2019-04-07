from django import forms
from .models import TransferCredit
from courses.models import Course


#We need a class where we are going to pass in something like "CHEM" and we're going to filter out those transfer credits with the "equivalentToDept" of CHEM 
#Should do some research on how to pass in variable into a class 
class TransferCategoryForm():

    categoryName = ''
    def __init__(self, *args, **kwargs):
        categoryName = kwargs.pop('cat')
        results = TransferCredit.objects.filter(equivalentToDept = categoryName)

        choices9 = []

        for i in results:
            # print(i.equivalentToID)
            choices9.append((i.equivalentToDept + ' ' + str(i.equivalentToID), i.name))

        super(TransferCategoryForm, self).__init__(*args, **kwargs)

        self.fields['tcID'].choices = choices9

        print(choices9)
        
    tcID = forms.MultipleChoiceField(
        required = False, 
        widget = forms.CheckboxSelectMultiple, 
        choices = []
    )
        



    

