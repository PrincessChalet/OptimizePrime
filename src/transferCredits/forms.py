from django import forms
from .models import TransferCredit
from courses.models import Course


#We need a class where we are going to pass in something like "CHEM" and we're going to filter out those transfer credits with the "equivalentToDept" of CHEM 
#Should do some research on how to pass in variable into a class 
class TransferCategoryForm(forms.Form):

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
        
class addCreditForm(forms.Form):
    #courseID = models.PositiveSmallIntegerField(null=True, blank=True)
    #courseDept = models.CharField(max_length=4,null=True, blank=True)
    #name = models.CharField(max_length=50)
    #equivalentToID = models.CharField(max_length=4, null=True, blank=True)
    #equivalentToDept = models.CharField(max_length=4, null=True, blank=True)
    #requiredScore = models.CharField(max_length=5, null=True, blank=True)
    #equivalentToCat = models.CharField(max_length=50, null=True, blank=True)

    courseID            = forms.IntegerField(label = 'Course ID', required = False)
    courseDept          = forms.CharField(label = 'Course Departement', required = False)
    name                = forms.CharField(label = 'Full Title with Course ID')
    equivalentToID      = forms.CharField(label = 'Equivalent Course ID', required = False) 
    equivalentToDept    = forms.CharField(label = 'Equivalent Course Department', required = False) 
    requiredScore       = forms.CharField(label = 'Required Score', required = False)
    equivalentToCat     = forms.CharField(label = 'Equivalent Category', required = False)


    

