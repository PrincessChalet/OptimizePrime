# This file holds utility functions for the degrees
from courses.models import Course, Prereq

from django.forms.models import model_to_dict

# needs the course array and the university core array
def timelineGenerator():

#*****************
# TEST values
    degreeCourses = ["MATH 1710", "MATH 1720", "TECM 2700", "CSCE 2100", "CSCE 2110", "CSCE 3110", "CSCE 4110", "CSCE 4444", "CSCE 4901"]
    coreCats = ["Communication", "Creative Arts", "Language, Philosophy, and Culture"]
#*****************


    # create the initial dictionary
    timeline = {0:[]}

    # here we loop through each course in the degree
    for i in degreeCourses:
        # call the recursive function
        coursePlacement(i, degreeCourses, coreCats, 0, timeline)

    print(timeline)

    # sort the dictionary before returning it
    for i in timeline:
        timeline[i].sort(key=priority, reverse=True)

    # return a dictionary that acts like a hash map
    return timeline

def findCourse(course, timeline):
    index = 0
    placed = False

    print(timeline)
    for i in timeline:
        innerIndex = 0
        if not timeline[i]:
            continue
        for j in timeline[i]:
            if j[0] == course:
                placed = True
                break
            innerIndex = innerIndex + 1
        if placed == True:
             break
        else: 
            index = index + 1

    return (placed, index, innerIndex)

def updatePriority(updateInfo, course, timeline):
    index = updateInfo[1]
    innerIndex = updateInfo[2]

    priority = timeline[index][innerIndex][1]

    temp = (course, priority + 1)

    timeline[index] = [entry for entry in timeline[index] if entry[0] != course]
    timeline[index].append(temp)

    return index

#**** need to solve an issue with the core courses
# needs the course, the course list, the corelist, the "offset", the dictionary
def coursePlacement(currentCourse, coursesList, coreList, offset, timeline):
    print("++++++++++ Current Course: " + currentCourse)
    #print(coursesList)
    tokens = currentCourse.split()
    
    checkCourse = Course.objects.filter(courseDept=tokens[0], courseID=tokens[1]).exists()
    print(checkCourse)

    if not checkCourse:
        print("The course does not exists. Return an error.")
        return -1

    # here we get the prereqs for a course in the courses list with a database call
    try:
    #    tokens = currentCourse.split()
        prereqs = Prereq.objects.filter(courseDept=tokens[0], courseID=tokens[1])


        # if the course does not have prereqs
        if not prereqs:
            # check if the course is already in the timeline
            inTimeline = findCourse(currentCourse, timeline)
            
            # if the course is already in the timeline
            if inTimeline[0]:
                # update the courses priority
                index = updatePriority(inTimeline)

                # return the location of the course in the timeline
                return index
            # else the current course is not in timeline
            else:
                # place it in the dictionary at location zero
                temp = (currentCourse,0)
                timeline[0].append(temp)
                
                return 0
        # else if the course has prereqs
        else:
            # assume the course is a leaf 
            leaf = True

            temp = model_to_dict(prereqs[0])
 #           print("test 1")

            largest = 0

            # for each prereq of currentCourse
            for i in temp["prereqCourses"]:
                print("***** Current prereq:  "+temp["prereqCourses"][i][0]) # test print
               
                #for j in temp["prereqCourses"][i]:
                #    print(j)
               
### check if the prereq is a core course here
                prereqName = temp["prereqCourses"][i][0]
                pTokens = prereqName.split()
                
                prereqCat = list(Course.objects.filter(courseDept=pTokens[0], courseID=pTokens[1]).values('category'))
                #prereqCat = Course.objects.filter(courseDept="TEST", courseID=1234).values('category')
                print(prereqCat[0]['category'])

                if not prereqCat:
                    print("empty list. The course isn't in the database. Must return error.")
                    return -1
                # if this prereq is not in the degree or a core course
                elif temp["prereqCourses"][i][0] not in coursesList and prereqCat[0]['category'] not in coreList:
                    # ignore this prereq
                    print("ignore this course") # test print
                # else this prereq is in the degree or is a core course
                else:
                    # the course is not a leaf
                    leaf = False

                    # recursively update the prereq's prereqs
                    placement = coursePlacement(temp["prereqCourses"][i][0], coursesList, coreList, 0, timeline)+1
                    
                    print(placement) # test print
                    # keep track of the largest placement since it determines the placement of the current course
                    if placement > largest:
                        largest = placement

            # check if the current course is already in the timeline
            x = findCourse(currentCourse, timeline)
 
            # if is already in the timeline
            if x[0]:
                # update the current course's priority
                index = updatePriority(x, currentCourse, timeline)
               
                return index
            else:
                # if the course is a leaf
                if leaf == True:
                # place this course at location 0
                    tempCourse = (currentCourse, 0)
                    timeline[0].append(tempCourse)
                    return 0
                # else the current course is not a leaf
                else:
                    tempCourse = (currentCourse, 0)
                  
                    # check if the largest placement is a valid key in the timeline dictionary
                    if largest not in timeline:
                        timeline[largest] = []
                  
                    # add the course to the timeline
                    timeline[largest].append(tempCourse)

                    # return largest value
                    return largest
       
    except:
        print('Error')

    return 0

def priority(x):
    return x[1]