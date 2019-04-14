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
        coursePlacement(i, degreeCourses, coreCats, timeline)

    #print(timeline) #test print

    # sort the dictionary before returning it
    for i in timeline:
        timeline[i].sort(key=priority, reverse=True)

    print(timeline) #test print
    # return a dictionary that acts like a hash map
    return timeline

# Description: A function used to find a course in the timeline
# Return:      The function returns the location of the course in the timeline and a boolean
#              representing whether it exists in the timeline or not
# Parameters:  course is a string of course such as CSCE 1030
#              timeline is a dictionary where each key holds a list of tuples
#              Ex. {1:[(CSCE 1030, 0, [])]}
def findCourse(course, timeline):
    index = 0 # the key of the timeline dictionary
    placed = False # assume course is not in the timeline

    #print(timeline) # test print

    # loop through each entry in the the timeline
    for i in timeline:
        innerIndex = 0 # the index of the course at key index
        
        # if the key is an empty array
        if not timeline[i]:
            continue
        
        # for each entry in the key
        for j in timeline[i]:
            # if the course is in the timeline
            if j[0] == course:
                placed = True 
                break

            innerIndex = innerIndex + 1 # move the index forward
        
        # if the course is in the timeline
        if placed == True:
            break
        # else increase the index
        else: 
            index = index + 1

    return (placed, index, innerIndex)

# Description: This function updates the second entry in a tuple.
#              Ex. (CSCE 1030, 0, []) this function would increase 0 to 1
# Return:      The index of the course, i.e. the key
# Parameters:  updateInfo is a tuple with a boolean value, a dictionary key, and a list index
#                   Ex. (True, 2, 3)
#              course is a string such as CSCE 1030
#              timeline is a dictionary of all the courses in the timeline
def updatePriority(updateInfo, course, timeline):
    index = updateInfo[1] # the key in timeline of course
    innerIndex = updateInfo[2] # the index in the list of key

    priority = timeline[index][innerIndex][1] # the courses priority
    prereqs = timeline[index][innerIndex][2] # the courses prereqs

    temp = (course, priority + 1, prereqs) # make a new tuple

    timeline[index] = [entry for entry in timeline[index] if entry[0] != course] # build a new list without the course
    timeline[index].append(temp) # add the tuple to the list

    return index # return the index

# needs the course, the course list, the corelist, the "offset", the dictionary
# Description: This function recursively finds the a courses prerequisites by querying the database
# Return:      a dictionary that acts as hash map of the location for each course
# Parameters:  currentCourse is a course in a list, the coursesList is the list of courses in the degree, coreList is
#              a list of the univeristy core categories, timeline is the preprocessed timeline
def coursePlacement(currentCourse, coursesList, coreList, timeline):
    print("++++++++++ Current Course: " + currentCourse)
    tokens = currentCourse.split()
    
    checkCourse = Course.objects.filter(courseDept=tokens[0], courseID=tokens[1]).exists()

    if not checkCourse:
        print("The course does not exists. Return an error.")
        return -1

    # here we get the prereqs for a course in the courses list with a database call
    try:
        prereqs = Prereq.objects.filter(courseDept=tokens[0], courseID=tokens[1])

        # if the course does not have prereqs
        if not prereqs:
            # check if the course is already in the timeline
            inTimeline = findCourse(currentCourse, timeline)
            
            # if the course is already in the timeline
            if inTimeline[0]:
                # update the courses priority
                index = updatePriority(inTimeline, currentCourse, timeline)

                # return the location of the course in the timeline
                return index
            # else the current course is not in timeline
            else:
                # place it in the dictionary at location zero
                temp = (currentCourse, 0, [])
                timeline[0].append(temp)
                
                return 0
        # else if the course has prereqs
        else:
            # assume the course is a leaf 
            leaf = True
            prereqArr = []

            temp = model_to_dict(prereqs[0])

            largest = 0

            # for each prereq of currentCourse
            for i in temp["prereqCourses"]:
                # check if the prereq is a core course
                prereqName = temp["prereqCourses"][i][0]
                pTokens = prereqName.split()
                prereqCat = list(Course.objects.filter(courseDept=pTokens[0], courseID=pTokens[1]).values('category'))

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

                    # ignore corerequisites since they can be taken at the same time
                    if i != 'C':
                        prereqArr.append(prereqName)

                    # recursively update the prereq's prereqs
                    placement = coursePlacement(temp["prereqCourses"][i][0], coursesList, coreList, timeline)+1
                    
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
                    tempCourse = (currentCourse, 0, [])
                    timeline[0].append(tempCourse)
                    return 0
                # else the current course is not a leaf
                else:
                    tempCourse = (currentCourse, 0, prereqArr)

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

# Description: a function used with python's list sort. The function takes a tuple parameter
# and uses it's second value to sort all tuples in a list
def priority(x):
    return x[1]

# this function needs to divide the timeline into the courses for each semester
# Description:  This function separates the timeline dictionary into groups of 5
# Return:       a list of lists of five entries where each entry is a course
# Parameter:    the timeline dictionary
def processTimeline(timeline):
    fullTimeline = [] # the processed timeline

    tempArr = [] # an array to append to the processed timeline
    index = 0 # the index of the timeline
    counter = 0 # a variable to count in fives
    total = 0 # the total of courses in level

    # while there are entries in the timeline to process
    while True:
        # if the current timeline level is not empty
        if timeline[index]:
            # add the course from the current level
            tempArr.append(timeline[index][total][0])
        # try to find courses in the next level
        else: 
            index = index + 1

        # check if the index is still valid
        if index == len(timeline):
            break
        
        counter = counter + 1 # move to the next entry in the current semester
        total = total + 1 # move to the next course

        # if the semester is full
        if counter == 5:
            counter = 0 # reset the counter
            fullTimeline.append(tempArr) # add the current semester to the timeline
            tempArr = [] # clear the contents of the temporary array

        # if there are no more courses in the current level
        if total == len(timeline[index]):

            # if there are spots that can be filled in the current semester
            if counter < 5 and index + 1 != len(timeline):

                # loop through the next course level
                for i,j,k in timeline[index + 1]:
                    canAdd = True # assume that the current course can be added to the current semester

                    # loop through the prereqs of courses in level + 1
                    for prereq in k:
                        # if the prereq is in the current semester
                        if prereq in tempArr:
                            # print("can't add: " + i) # test print
                            canAdd = False # can't add this course
                            
                    # if the course can be added to the timeline
                    if canAdd:
                        tempArr.append(i) # add the course to the current semester
                        timeline[index+1].remove((i,j,k)) # remove the course from the timeline at level + 1
                        counter = counter + 1 # increase the counter
                        
                        # if there are no more course spaces in the current semester
                        if counter == 5: 
                            break

            fullTimeline.append(tempArr) # add the semester to the timeline
            index = index + 1 # move to the next level in the timeline

            # reset variable
            tempArr = []
            total = 0 
            counter = 0

        # check if the index is still valid
        if index == len(timeline):
            break
    
    # if the semester has courses 
    if tempArr:
        fullTimeline.append(tempArr) # add the semester to the timeline

    return fullTimeline # return the processed timeline

# Description:  The function takes a degree object and generates a dictionary where
#               each key is a course and each value is a course's database information
# Return:       A dictionary that maps courses with their database information
# Parameter:    A degree database object as a dictionary
def courseDescriptionStructure(degree):

    courseDescriptions = {}

    # iterate through the object and find the specific courses
    for courseList in degree['degreeInfo'].values():
        for element in courseList:
            if type(element) is list:
                for course in element:
                    if '*' not in course:
                        courseDescriptions[course] = generateCourseInfo(course)
            elif type(element) is str:
                course = element
                if '*' not in course:
                    courseDescriptions[course] = generateCourseInfo(course)
            elif type(element) is dict:
                subcategory = element
                for subCatCourseList in subcategory.values():
                    for entry in subCatCourseList:
                        if type(entry) is list:
                            for course in entry:
                                if '*' not in course:
                                    courseDescriptions[course] = generateCourseInfo(course)
                        elif type(entry) is str:
                            course = entry
                            if '*' not in course:
                                courseDescriptions[course] = generateCourseInfo(course)

    return courseDescriptions

    
# Description:  This function is used to build a string the represents the information for a particular course
# Return        A string which holds the parameters information the information is the course's name,
#               the number of the course's hours, and the course's description
# Parameter:    the course department and course id as a single string, i.e. CSCE 1030   
def generateCourseInfo(course):

    # split the course string
    tokens = course.split(' ')

    # query the database for the course
    courseObj = Course.objects.filter(courseDept=tokens[0], courseID=tokens[1])
    courseObj = model_to_dict(courseObj[0])

    # build the course's info string
    courseInfo = courseObj['name'] + ' ' + str(courseObj['hours']) + ' hours\n'
    courseInfo = courseInfo + '\n' + courseObj['description']

    return courseInfo

# Description:  This funciton generates a dictionary entry
# Return        a a string and list of courses - tuple of a list of courses and a string ()
# Parameter:    a JSON object, and degree name  
def generateDictEntry(degreeCore,degreeName,category,lookUpCat):
    coreCourses = []
    idString = '*_'
    print(degreeCore)
    print(degreeName)
    
    counter = 0
    for cat in degreeCore[lookUpCat]:
        if cat == 'Universal':
            for course in degreeCore[lookUpCat][cat]:
                counter = counter +1
                coreCourses.append(course)
        elif cat == degreeName:
            for course in degreeCore[lookUpCat][cat]:
                counter = counter +1
                if type(course) is list:
                    estring = ''
                    for c in course:
                        estring = estring + c + ' '
                    coreCourses.append(estring)
                else:
                    coreCourses.append(course)
                    #counter = counter + 1
    idString = idString + str(counter) + '-@' + category
    return (idString,coreCourses)