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

import json

# Create your views here.
# this is where you transfer data from the data base to the html page /where you recieve the information from the checkboxes form

def transferCreditView(request):

    if request.method == 'POST':
        # We build the form 
        #print(request.POST)
        #print(request.POST.get('transfer credits', ''))
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        transferCredits = body['transfer credits'] 

    equivalencyMap = generateTCListByCategory() 
        
    #    return render(request, 'degree/transferCreditList.html', { "context": tempContext })
    return render(request, 'degree/transferCreditList.html', { 'equivalencyList': equivalencyMap})