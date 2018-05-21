# Functions

# Create a function
def sayHello(name = 'Developer'): #  function with default value
    print('Hello', name)

sayHello('Sivar')

# Return a value
def getSum(num1, num2):
    total = num1 + num2
    return total

numSum = getSum(44, 54)
print(numSum)

# Add One to a number
def addOneToNum(num):
    num = num + 1
    print('Value inside function is ', num)
    return

num = 5
addOneToNum(num)
print('Value outside function is ', num)

def addOneToList(myList):
    myList.append(4)
    print('Value inside function is ', myList)
    return

myList = [1,2,3]
addOneToList(myList)
print('Value outside function is ', myList)