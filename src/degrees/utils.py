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
    coursePlacement("CSCE 3110", degreeCourses, coreCats, 0, timeline)
    coursePlacement("CSCE 4444", degreeCourses, coreCats, 0, timeline)
    print(timeline)
        # call the recursive function

        # get a return value

    # sort the dictionary before returning it

    # return a dictionary that acts like a hash map
    return timeline

def findCourse(course, timeline):
    index = 0
    placed = False

    for i in timeline:
        innerIndex = 0
        for j in timeline[i]:
            if j[0] == course:
                placed = True
                break
            innerIndex = innerIndex + 1
        if placed == True: break
        index = index + 1

    return (placed, index, innerIndex)

def updatePriority(updateInfo, course, timeline):
    index = updateInfo[1]
    innerIndex = updateInfo[2]

    priority = timeline[index][innerIndex][1]

    temp = (course, priority + 1)

    timeline[index] = [entry for entry in timeline[index] if entry[0] != course]

    return index

#**** need to solve an issue with the core courses
# needs the course, the course list, the corelist, the "offset", the dictionary
def coursePlacement(currentCourse, coursesList, coreList, offset, timeline):
    print(currentCourse)
    #print(coursesList)
    
    # here we get the prereqs for a course in the courses list with a database call
    try:
        tokens = currentCourse.split()
        prereqs = Prereq.objects.filter(courseDept=tokens[0], courseID=tokens[1])

        # if the course does not have prereqs
        if not prereqs:

            index = 0 # the index in the dictionary
            placed = False
            for i in timeline:
                innerIndex = 0 # the index in the list of a dictionary
                for j in timeline[i]:
                    if j[0] == currentCourse:
                        placed = True
                        break
                    innerIndex = innerIndex + 1
                if placed == True: break
                index = index + 1

            print(placed)
            # if the course is already on the timeline
            if placed:
                # update priority
                print('must update priority')
                tempCourseID = timeline[index][innerIndex][0]
                tempCoursePriority = timeline[index][innerIndex][1]+1
                temp = (tempCourseID, tempCoursePriority)
               
                timeline[index] = [entry for entry in timeline[index] if entry[0] != tempCourseID]
                timeline[index].append(temp)

                return index
                # return 0 or the level?
            # else the current course is not in timeline
            else:
                temp = (currentCourse,0)
                timeline[0].append(temp)
                # place it in the dictionary at location 1 or zero
                # return a 1
                return 0
        # else if the course has prereqs
        else:
            # assume the course is a leaf 
            leaf = True

            temp = model_to_dict(prereqs[0])
            print(temp)

            largest = 0
            # for each prereq of currentCourse
            for i in temp["prereqCourses"]:
                print(temp["prereqCourses"][i][0]) # test print
               
                #for j in temp["prereqCourses"][i]:
                #    print(j)
               
                # if this prereq is not in the degree or a core course
                if temp["prereqCourses"][i][0] not in coursesList:
                    print("ignore this course")
                    # ignore this course
                # else this prereq is in the degree or is a core course
                else:
                    # the course is not a leaf
                    leaf = False

                    # recursively update the prereq's prereqs
                    placement = coursePlacement(temp["prereqCourses"][i][0], coursesList, coreList, 0, timeline)+1
                    
                    print(placement)
                    # keep track of the largest return value because the current course requires the largest placement
                    if placement > largest:
                        largest = placement

            # if the course is a leaf
            if leaf == True:
                # place this course at location 1
                temp = (currentCourse, 0)
                timeline[0].append(temp)
                return 0

            # but I can take care of the assignment here

            temp = (currentCourse, 0)
            timeline[largest] = temp
            # return largest value
            return largest
       
    except:
        print('Error')

    return 0