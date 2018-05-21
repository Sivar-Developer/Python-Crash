# Conditions

x = 4

# Basic if
if x < 6:
    print('This is True')

if x < 6:
    print('This is True')
print('This text not part of if condition') # No Indentation

# if else
if x < 2:
    print('This is True')
else:
    print('This is False')

# Elif
color = 'red'

if color == 'red':
    print('Color is red')
elif color == 'blue':
    print('Color is Blue')
else:
    print('Color is not red or blue')

# Nested If Statments
if color == 'red':
    if x < 10:
        print('Color is red and x is less than 10')

# Logical Operators
if color == 'red' and x < 10:
    print('Color is red and x is less than 10')