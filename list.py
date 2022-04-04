testList = [50, 100, 'Laurence', 'Hello', 50, 100, True]
#print(testList)

# Duplicates ARE allowed
# Items in list ARE 0-indexed and can be accessed using square brackets
#print(testList[2])

# Variables can be assigned to values in the list using commas
# HOWEVER, there must be the same number of variables as there are elements in the list
# ----> a, b, c = testList results in error
a, b, c, d, e, f, g = testList

# Can get length of list using len()
#print(len(testList))

# Can access elements in list using negative indexes
#print(testList[-1], testList[-2])

# Can access range of elements in list using colon
# Is NOT INCLUSIVE of second value
#print('testList[1:3]', testList[1:3]) # i.e. returns two values, those at index 1 and 2 NOT 3

# Can use no number at start to return everything up to what you specify after
# THIS **annoyingly** INCLUDES THE VALUE AT THE INDEX YOU SPECIFY
#print('testList[:3]', testList[:3])

# Can insert values using testList.insert(index, value)
testList.insert(2, 'Svekis')
#print(testList)

# Can add to the end using testList.append(value)
testList.append('End')
#print(testList)

# Can update values by simply reassigning at an index
testList[0] = "New Value"
#print(testList)

# Can get the index of the first item with a value using index
#print(testList.index('Hello'))

# Can check if something is in the list by using 'val = (value in list)'
val = ("Svekis" in testList)
#print(val)

# Can remove item from the list using .remove(value)
testList.remove(100)
#print(testList)

# Can remove last value using pop(), or specific index via pop(index)
lastValue = testList.pop()
secondValue = testList.pop(1)
#print(lastValue, secondValue, testList)

#Can sort using sort()
# This must be used on lists containing ONLY numbers OR strings
alphanumericList = [1, 50, 3, 8]
alphanumericList.sort()
#print(alphanumericList)

# can reverse lists using reverse
alphanumericList.reverse()
#print(alphanumericList)

# Can copy lists using copy
copiedList = alphanumericList.copy()
#print(copiedList)

# Copy makes a true copy, if you modify the copy the original WON'T change
copiedList.append('See? I know what I\'m talking about lad')
print(copiedList, alphanumericList)  

# Can also delete items from list by using 'del testList[index]'
del testList[1]
#print(testList)

# Can also delete entire list using the same method by not using an index
del testList
#print(testList)

