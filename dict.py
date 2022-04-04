# Initialised using curly braces, but differ from sets in that they have key-value pairs
testDict = {'first': 'value', 'second': {'one': 'test', 'two': 'test2'}, 'third': True}

# They're not indexed as they use the key
# The order won't change, it will be what you set it as
# Items in a dictionary can be accessed by referencing the key in square brackets
val = testDict['first']

# Can update value by simply reassigning at the key level
testDict['first'] = 'Hello World'

# Nested values can be accessed as you'd expect
nested = testDict['second']['two']

# Can add values by referencing a new key and setting a value to it

testDict['new'] = 'new value'

# Can remove items by using pop(key)
testDict.pop('first')

# Can use .clear() to completely remove everything from a dictionary
testDict.clear()
print(testDict)

testDict['one'] = 'Hello'
testDict['two'] = 'World'
testDict['bool'] = True
testDict['int'] = 100

# The .keys() method will return the keys
keys = testDict.keys()

# The .values() method will return the values
values = testDict.values()
print(values)