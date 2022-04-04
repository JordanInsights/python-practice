# Integer
a = 5

# String
b = 'hello'

# Boolean - MUST BE CAPITALIZED
c = True
d = False
e = 5 > 10

# Lists - store multiple items in one variable 
# One of the FOUR data types in python to store collections of data

testList = [50, "50", True, 50]

#Data type of list is list
print('List', testList) 

# Can find out length by using length method
lengthOfList = len(testList)

# Tuples are similar to lists but it is a collection that is ORDERED and UNCHANGEABLE
# Initialised with parentheses

testTuple = (50, '50', True, 50)
print('Tuple', testTuple)

# Sets are another type of collection, but they DON'T ALLOW DUPLICATES and they are UNORDERED
# Or rather, that they order themselves, not the order you specify
# Initialised with curly braces
testSet = {50, '50', True, 50}
print('Set', testSet)

# Dictionaries also use curly braces, but they use key-value pairs
testDictionary = {'first': 50, 'second': '50', 'third': True, 'fourth': 50}
# They ARE ORDERED 
print('Dictionary', testDictionary)

