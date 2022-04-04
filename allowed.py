age = input("How old are you? ")
bool = age.isnumeric()

if bool:
    num = int(age)
    if(num >= 18):
        print('Great, you\'re of legal drinking age. Drink to your heart\'s content lad')
    elif(num >= 16):
        print('You can come in, but I better not catch you with any pints')
    else:
        print('You\'re not allowed in kiddo')
else: 
    print('We need your age!')
