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

#import the TransferCredit model
from .utils import generateTCListByCategory

from degrees.utils import processChoices

import json

# Create your views here.
# this is where you transfer data from the data base to the html page /where you recieve the information from the checkboxes form

def transferCreditView(request):

    if request.method == 'POST':
<<<<<<< HEAD
        request.session['transferCredit'] = request.POST.getlist('transfer credits')
=======
        tempTransferCredits = request.POST.getlist('transfer credits')

        if 'transferCredit' in request.session:
            result = processChoices(request.session['transferCredit'],tempTransferCredits)
        else:
            result = processChoices([], tempTransferCredits)
        request.session['transferCredit'] = result
            
>>>>>>> 7a3581f5c565c19beb8004c851de7e6465d89a8b
        print(request.session['transferCredit'])

    myList = request.POST.getlist('transfer credits')
    equivalencyMap = generateTCListByCategory() 
        
    #    return render(request, 'degree/transferCreditList.html', { "context": tempContext })
    return render(request, 'degree/transferCreditList.html', {'equivalencyList': equivalencyMap})

    