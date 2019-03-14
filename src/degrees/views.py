from django.shortcuts import render

#import the degrees model
from .models import Degree
from .forms import DegreeSelectionForm

#adding something to create a model to dict
from django.forms.models import model_to_dict
from .utils import timelineGenerator

# Create your views here.
# Description: This function generates a dropdown form so that he users
#              can select a degree
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
          
          print(choice[0].degreeInfo) # test print
          request.session['degree']=model_to_dict(choice[0])
           
        except Degree.DoesNotExist:
          print('invalid selection')
      else:
        print('invalid choice')

    degreeDropdown = DegreeSelectionForm()

    return render(request, 'degree/degreeList.html', { 'form': degreeDropdown })

#This is the function for structure for saving user info @CHALET
def degreeClassesView(request):

    if request.session.get('degree'):
      print(request.session.get('degree'))
      print('Degree Set')
    else:
      print('Need a degree')

    sampleContext = {'name': "Computer Science"}

    return render(request, 'degree/degreePlan.html', sampleContext)

# Description: This function determines which courses need will be
#              shown in the timeline view
def degreeTimeline(request):
    # here we use the degree that the user has already selected
    # not sure if we would need to ask for the degree object again


    ### assume we extracted all the classes from the JSON degree object
    ### and placed them in a list. 
    ### Might make CHALET add that to the JSON objetcs
    degreeCourses = ["MATH 1710", "MATH 1720", "TECM 2700", "CSCE 2100", "CSCE 2110", "CSCE 3110", "CSCE 4110", "CSCE 4444", "CSCE 4901"]

    sampleContext = {'name': 'Computer Science'}

    timeline = timelineGenerator()

    print("Finished setting the timeline\n\n")
    print(timeline)

    return render(request, 'degree/timeline.html', {'timeline': timeline})