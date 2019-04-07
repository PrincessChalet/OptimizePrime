from django.shortcuts import render

#import the degrees model
from .models import Degree

# import the forms
# the right form is not used anymore
from .forms import DegreeSelectionForm, CoursesSelectionForm

# import the courses model
from courses.models import Course

#adding something to create a model to dict
from django.forms.models import model_to_dict
from .utils import timelineGenerator, processTimeline, courseDescriptionStructure

# Create your views here.
# Description: This function generates a dropdown form so that he users
#              can select a degree
def allDegreesView(request):
   
    # need to figure out stuff about default values
    if request.method == 'POST':
      degreeChoice = DegreeSelectionForm(request.POST)
      mathForm = ['MATH']
      test = CoursesSelectionForm(request.POST, test=mathForm)

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

    if request.method == 'POST':
        print(request.POST)

    #the context needs to change depending of whether the user has a degree or not
    if request.session.get('degree'):
      #print(request.session.get('degree'))
      print('Degree Set')
      usersDegree = request.session.get('degree')
      # if the degree is set get the JSON objects

    else:
      print('Need a degree')
      # redirect to other page pass empty context?

    # seems like the degree context will need a degree name
    # somehow we need to map each course description with the database
    details = courseDescriptionStructure(usersDegree)

    # the code below should go in the utility function 
    temp = Course.objects.filter(courseID = 1030, courseDept="CSCE")
    temp = model_to_dict(temp[0])
    tempDict = {temp['courseDept'] + " " + str(temp['courseID']) : temp['description']}

    tempContext = {
        "degree": usersDegree,
        "coursesInfo" : details,
    }

    return render(request, 'degree/degreePlan.html', { "context": tempContext })

# Description: This function determines which courses need will be
#              shown in the timeline view
def degreeTimeline(request):
    # here we use the degree that the user has already selected
    # not sure if we would need to ask for the degree object again


    ### assume we extracted all the classes from the JSON degree object
    ### and placed them in a list.
    degreeCourses = ["MATH 1710", "MATH 1720", "TECM 2700", "CSCE 2100", "CSCE 2110", "CSCE 3110", "CSCE 4110", "CSCE 4444", "CSCE 4901"]

    sampleContext = {'name': 'Computer Science'}

    timeline = timelineGenerator()

    #print("Finished setting the timeline\n\n")
    #print(timeline)
    
    fullTimeline = processTimeline(timeline)
    #print(fullTimeline)
#******** need to further refine the timeline here before passing it to the view
#******** need another util function

    #return render(request, 'degree/timeline.html', {'timeline': timeline})
    return render(request, 'degree/timeline.html', {'timeline': fullTimeline})