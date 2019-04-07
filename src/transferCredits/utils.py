from .models import TransferCredit

#FUNCTION: Generate tuples list (equivalentCredit, transferCredit)
def generateEquivalencyList(categoryName):

    results = TransferCredit.objects.filter(equivalentToDept = categoryName)

    equivalencyList = []

    for i in results:
        #(equivalentCredit, transferCredit)
        equivalencyList.append((i.equivalentToDept + ' ' + str(i.equivalentToID), i.name))

    return equivalencyList

#FUNCTION: Loop through array of categories ("Biology", "Communication", etc.) and get the tuples list for each one 
def generateTCListByCategory():
    
    #Array of category names 
    categoriesLong = ['Technincal Writing', 'Computing/Programming', 'Engineering', 'Biology', 'Chemistry', 'Physics', 'Mathematics']

    #Array of category "departments"
    categoriesShort = ['TECM', 'CSCE', 'ENGR', 'BIOL', 'CHEM', 'PHYS', 'MATH']

    #
    equivalencyMap = {} 
    indexCounter = 0

    #equivalencyMap['TECM'] = generateEquivalencyList(categoriesShort[4])

    #Iterate through department categories 
    for element in categoriesShort:
        #Get the equivalency list for this specific department / category by calling function: generateEquivalencyList()
        equivalencyMap[categoriesLong[indexCounter]] = generateEquivalencyList(element)

        indexCounter = indexCounter + 1; 


    return equivalencyMap