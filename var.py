#Declare variables
a = 5
b = 10
print(a+b)

# Convert to String
a = str(a)
print(a, type(a))

#Convert to integer
a = int(a)
print(a, type(a))

#Variable names must start with a letter or an underscore
#Characters must be alphanumeric

# You can comma separate to declare multiple variables
a, b, c = 1 , 10 , 100
print(a, b, c)

# Can upack variables in a similar manner
a, b, c = ['John', 'Peter', 'Jake']
print (b)

# You can assign the same value to multiple variables at the same time
d = e = f = 1000
print(d, e, f)