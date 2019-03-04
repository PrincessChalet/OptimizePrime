from django.shortcuts import render

#import the degrees model
from .models import Degree

# Create your views here.
def allDegreesView(request):
    # we would use the line below to get all the degrees from the database
    # degreesList = Degree.objects.all()

    # the line below is a sample context normally we would have
    # context = { degreeList } I think
    context = { 'name' : "Computer Science"}

    return render(request, 'degree/degreeList.html', context)

def degreeClassesView(request):
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