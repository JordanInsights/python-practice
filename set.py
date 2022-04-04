# Sets are initialised using curly braces
# They are unordered
# Values CANNOT BE CHANGED, they can only be ADDED or REMOVED

testSet = {'Svekis', 100, True, 'Laurence', 100, 100, True}
print(testSet)

# Values can be added using add()
testSet.add('New Value')
print(testSet)

# Values can be removed by using remove(value)
testSet.remove(100)
print(testSet)

# Items can be removed randomly using pop()
testSet.pop()
print(testSet) 

# Can check if an item is in a set using (value in set)
val = ('Svekis' in testSet)
print(val)