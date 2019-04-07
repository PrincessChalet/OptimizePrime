from django.shortcuts import render

# import the courses model
from courses.models import Course

# import the transfer form?
from .forms import TransferCategoryForm

#import the TransferCredit model
from .models import TransferCredit

#adding something to create a model to dict
from django.forms.models import model_to_dict
#from .utils import timelineGenerator, processTimeline, courseDescriptionStructure


# Create your views here.
# this is where you transfer data from the data base to the html page 

def transferCreditView(request):
    temp = TransferCredit.objects.all()

    #look at objects.filter / look at the parameters  

    array = ['CHEM']

    if request.method == 'POST':
        # We build the form 

        testForm = TransferCategoryForm(request.POST, cat = array[0])

    testForm = TransferCategoryForm(cat = array[0])
        
    #    return render(request, 'degree/transferCreditList.html', { "context": tempContext })
    return render(request, 'degree/transferCreditList.html', { "form": testForm })