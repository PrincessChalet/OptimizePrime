from django.shortcuts import render

#import the degrees model
from .models import Degree

# import the forms
from .forms import DegreeSelectionForm, CoursesSelectionForm

# import the courses model
from courses.models import Course

#adding something to create a model to dict
from django.forms.models import model_to_dict
from .utils import timelineGenerator, processTimeline, degreeViewStructure

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

    if request.method == 'POST':
        print(request.POST)

        #checks = CoursesSelectionForm(request.POST)

        #if checks.is_valid():
        #    cleanedChecks = checks.cleaned_data
        #    print(cleanedChecks)
        #else:
        #    print("error")

    # assume we fetched the core requirements i.e. Math, Science, ...
    coreRequirements = {
      "engineering requirements": [
        {
            "Technical Communications": {
                "Computer Science": [
                    "TECM 4100",
                    "TECM 4180",
                    "TECM 4190",
                    "TECM 4200",
                    "TECM 4250"
                ],
                "Technical Communications": "TECM 2700"
            }
        },
        {
            "Mathmatics": {
                "BIO": [
                    "MATH 1710",
                    "MATH 1720",
                    "MATH 2700",
                    [
                        "MATH 2730",
                        "MATH 3350"
                    ],
                    "MATH 3410",
                    "MATH 3680"
                ],
                "CE": [
                    "MATH 1710",
                    "MATH 1720",
                    "MATH 1780",
                    "MATH 2700",
                    "MATH 3410"
                ],
                "Computer Science": [
                    "MATH 1710",
                    "MATH 1720",
                    "MATH 1780",
                    "MATH 2700"
                ],
                "Construction": [
                    "MATH 1710",
                    "MATH 1720"
                ],
                "EE": [
                    "MATH 1710",
                    "MATH 1720",
                    "MATH 2730",
                    "MATH 2700",
                    "MATH 3410",
                    "MATH 3680"
                ],
                "Information Technology": [
                    "MATH 1710",
                    [
                        "MATH 1680",
                        "MATH 1780"
                    ]
                ],
                "MEE": [
                    "MATH 1710",
                    "MATH 1720",
                    "MATH 2700",
                    "MATH 2730",
                    "MATH 3410"
                ],
                "MET": [
                    "MATH 1710",
                    "MATH 1720"
                ],
                "Material": [
                    "MATH 1710",
                    "MATH 1720",
                    "MATH 2700",
                    "MATH 3410"
                ]
            }
        },
        {
            "Science": {
                "BIO": [
                    [
                        "BIOL 2301",
                        "BIOL 2311"
                    ],
                    [
                        [
                            "CHEM 1410",
                            "CHEM 1430"
                        ],
                        [
                            "CHEM 1415",
                            "CHEM 1435"
                        ]
                    ],
                    [
                        "PHYS 1710",
                        "PHYS 1730"
                    ]
                ],
                "CS": [
                    [
                        "PHYS 1710",
                        "PHYS 1730"
                    ],
                    [
                        "PHYS 2220",
                        "PHYS 2240"
                    ],
                    [
                        [
                            "CHEM 1410",
                            "CHEM 1430"
                        ],
                        [
                            "CHEM 1415",
                            "CHEM 1435"
                        ],
                        [
                            "CHEM 1420",
                            "CHEM 1440"
                        ],
                        "BIOL 1710",
                        "BIOL 1720",
                        "BIOL 1760"
                    ]
                ],
                "Construction": [
                    [
                        "PHYS 1710",
                        "PHYS 1730"
                    ],
                    [
                        "PHYS 2220",
                        "PHYS 2240"
                    ],
                    "CHEM 1410",
                    "CHEM 1430"
                ],
                "IT": [
                    [
                        "PHYS 1710",
                        "PHYS 1730"
                    ],
                    [
                        [
                            "CHEM 1410",
                            "CHEM 1430"
                        ],
                        [
                            "CHEM 1415",
                            "CHEM 1435"
                        ],
                        [
                            "BIOL 1710",
                            "BIOL 1760"
                        ]
                    ]
                ],
                "Material": [
                    [
                        "CHEM 1410",
                        "CHEM 1430"
                    ],
                    "CHEM 1420",
                    [
                        "PHYS 1710",
                        "PHYS 1730"
                    ],
                    [
                        "PHYS 2220",
                        "PHYS 2240"
                    ],
                    "PHYS 3010"
                ],
                "Science": [
                    [
                        "PHYS 1710",
                        "PHYS 1730"
                    ],
                    [
                        "PHYS 2220",
                        "PHYS 2240"
                    ],
                    [
                        [
                            "CHEM 1410",
                            "CHEM 1430"
                        ],
                        [
                            "CHEM 1415",
                            "CHEM 1435"
                        ]
                    ]
                ]
            }
        }
    ]
   }
    # assume we retrieved the computer science courses
    degreeRequirements = {
                "Computer Science and Engineering": [
                    "CSCE 1030",
                    "CSCE 1040",
                    "CSCE 2100",
                    "CSCE 2110",
                    "CSCE 2610",
                    "CSCE 3110",
                    "CSCE 3600",
                    "CSCE 4010",
                    "CSCE 4110",
                    "CSCE 4444",
                    [
                        "CSCE 4901",
                        "CSCE 4999"
                    ]
                ],
                "Computer Science and Engineering Breadth Elctivies": [
                    [
                        "CSCE 4210",
                        "CSCE 4230",
                        "CSCE 4240",
                        "CSCE 4290",
                        "CSCE 4310",
                        "CSCE 4350",
                        "CSCE 4460",
                        "CSCE 4550"
                    ],
                    [
                        "CSCE 4210",
                        "CSCE 4230",
                        "CSCE 4240",
                        "CSCE 4290",
                        "CSCE 4310",
                        "CSCE 4350",
                        "CSCE 4460",
                        "CSCE 4550"
                    ]
                ],
                "Computer Science and Engineering Core Elctivies": [
                    [
                        "CSCE 3530",
                        "CSCE 4115",
                        "CSCE 4430",
                        "CSCE 4600",
                        "CSCE 4650"
                    ],
                    [
                        "CSCE 3530",
                        "CSCE 4115",
                        "CSCE 4430",
                        "CSCE 4600",
                        "CSCE 4650"
                    ]
                ],
                "Computer Science and Engineering Free Electivies": [
                    [
                        "CSCE 4890",
                        "CSCE 4920",
                        "CSCE 4930",
                        "CSCE 4940",
                        "CSCE 4950"
                    ],
                    [
                        "CSCE 4890",
                        "CSCE 4920",
                        "CSCE 4930",
                        "CSCE 4940",
                        "CSCE 4950"
                    ],
                    [
                        "CSCE 4890",
                        "CSCE 4920",
                        "CSCE 4930",
                        "CSCE 4940",
                        "CSCE 4950"
                    ]
                ],
                "Electrical Engineering": ["EENG 2710"]
    }

    #degreeViewStructure({}, degreeRequirements)


    #the context needs to change depending of whether the user has a degree or not
    if request.session.get('degree'):
      #print(request.session.get('degree'))
      print('Degree Set')
      # if the degree is set get the JSON objects

    else:
      print('Need a degree')
      # redirect to other page?

    test = CoursesSelectionForm()


    # seems like the degree context will need a degree name
    # somehow we need to map each course description with the database
    degreeContext = {
                "Computer Science and Engineering": [
                    "CSCE 1030",
                    "CSCE 1040",
                    "CSCE 2100",
                    "CSCE 2110",
                    "CSCE 2610",
                    "CSCE 3110",
                    "CSCE 3600",
                    "CSCE 4010",
                    "CSCE 4110",
                    "CSCE 4444",
                    [
                        "CSCE 4901",
                        "CSCE 4999"
                    ]
                ]
    }

    temp = Course.objects.filter(courseID = 1030, courseDept="CSCE")
    temp = model_to_dict(temp[0])
    print(temp)
    tempDict = {temp['courseDept'] + " " + str(temp['courseID']) : temp['description']}
    print(tempDict)

    tempContext = {
        "degree": degreeContext,
        "courseDescriptions" : tempDict,
    }

    #return render(request, 'degree/degreePlan.html', {'degree': degreeContext})
    return render(request, 'degree/degreePlan.html', { "context":tempContext })

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