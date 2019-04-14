from django.shortcuts import render

#import the degrees model
from .models import Degree

# import the forms
# the right form is not used anymore
from .forms import DegreeSelectionForm, CoursesSelectionForm

# import the courses model; allows us to query DB
from courses.models import Course
from tecmCore.models import TechClasses
from mathCore.models import MathClasses

#adding something to create a model to dict
from django.forms.models import model_to_dict
from .utils import timelineGenerator, processTimeline, courseDescriptionStructure, generateDictEntry

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
          request.session['degree']=model_to_dict(choice[0])
          degreeName = request.session.get("degree")['name']

          # get the technical communications courses
          techcourses = TechClasses.objects.filter(name="Engineering TECM")
         # print(techcourses)
          techcourses = model_to_dict(techcourses[0])
        #  print(techcourses)
          tecm = generateDictEntry(techcourses, degreeName, "Technical Communications", "tecmCoreInfo")
          request.session.get('degree')['degreeInfo'][tecm[0]] = tecm[1]

          # get the mathematics courses 
          mathcourses = MathClasses.objects.filter(name="Engineering MATH")
          mathcourses = model_to_dict(mathcourses[0])
          math = generateDictEntry(mathcourses, degreeName, "Mathematics", "mathCoreInfo")
          request.session.get('degree')['degreeInfo'][math[0]] = math[1]
          print(request.session.get('degree'))
       #   print(choice[0].degreeInfo) # test print
         
           
        except Degree.DoesNotExist:
          print('invalid selection')
      else:
        print('invalid choice')

    degreeDropdown = DegreeSelectionForm()

    return render(request, 'degree/degreeList.html', { 'form': degreeDropdown })

#This is the function for structure for saving user info @CHALET
def degreeClassesView(request):

    if request.method == 'POST':
        degreeName = request.session.get("degree")['name']
        request.session['taken'] = request.POST.getlist(degreeName)
        print(request.POST)
        print(request.session.get("taken"))
        



    #the context needs to change depending of whether the user has a degree or not
    if request.session.get('degree'):
      #print(request.session.get('degree'))
      print('Degree Set')
      usersDegree = request.session.get('degree')
      
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
      } # if the degree is set get the JSON objects  
    else:
      print('Need a degree')
      tempContext = {}
      # redirect to other page pass empty context?

    

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