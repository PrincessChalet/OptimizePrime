from django.shortcuts import render

#import the degrees model
from .models import Degree
from .forms import DegreeSelectionForm

#adding something to create a model to dict
from django.forms.models import model_to_dict

# Create your views here.
def allDegreesView(request):
   
    # need to figure out stuff about default values
    if request.method == 'POST':
      degreeChoice = DegreeSelectionForm(request.POST)

      # The code below is used to get the user's input
      if degreeChoice.is_valid():
        cleanedChoice = degreeChoice.cleaned_data

        # when accessing objects we will need try/except blocks 
        try:
          choice = Degree.objects.filter(name=cleanedChoice['degreeChoices'])
          
          print(choice[0].degreeInfo)
          request.session['degree']=model_to_dict(choice[0])
           
        except Degree.DoesNotExist:
          print('invalid selection')
      else:
        print('invalid choice')

    degreeDropdown = DegreeSelectionForm()

    return render(request, 'degree/degreeList.html', { 'form': degreeDropdown })

def degreeClassesView(request):

    if request.session.get('degree'):
      print(request.session.get('degree'))
      print('Degree Set')
    else:
      print('Need a degree')
    # here we would ask for a specific degree so something like
    # degree = Degree.objects.get(name='userInputDegree')

    sampleContext = {'name': "Computer Science"}
  #  sampleContext = {'name': "Computer Science",
   #                  'Core Sections' : ['Communications', 'Creative arts'],
    #                 'Requirements' : [
     #                                   'Mathematics' : ['MATH 1010', 'Math 1020'],
      #                                  'Science' : ['BIOL 1010'],
       #                                   ]
        #            }

    return render(request, 'degree/degreePlan.html', sampleContext)

def degreeTimeline(request):
    # here we use the degree that the user has already selected
    # not sure if we would need to ask for the degree object again
    sampleContext = {'name': 'Computer Science'}

    return render(request, 'degree/timeline.html', sampleContext)