# IF, IF ELSE, and ELSE are as follow
boo = True
a = 500
b = 1000

if boo:
    print('Boo is True')

if not(boo):
    print("You won't see this")
else:
    print("You will see this")

if not(boo):
    print('You won\'t see this')
elif b > a:
    print('This condition passes')

# Other Syntax:
print('Hello') if a < b else print('Something else')

print("Equal") if a == b else print("A is bigger") if a > b else print("B must be bigger")