val = input('What is your favourite number 1-9: ')
boo = val.isnumeric()
message = "Sorry, " + val + " is not a number "
if(boo):
    num = int(val)
    message = "Great your number is " + val
    validNumber = num > 0 and num < 10

    if(not(validNumber)):
        message = "Sorry, " + val + " is not between 1 and 9"
print(message)