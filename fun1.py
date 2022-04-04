def multiplyByTen(num):
    return num * 10

num = input("Enter a number to muliply by ten: ")
numIsNumeric = num.isnumeric()

if(not(numIsNumeric)):
    print('You must enter a number')
else:
    num = int(num)
    mutlipliedValue = multiplyByTen(num)
    str = str(num) + ' * 10 = ' + str(mutlipliedValue)
    print(str)

