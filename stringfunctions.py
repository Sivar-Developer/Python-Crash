# String Functions

myStr = 'hello World'

# Capitalize
print(myStr.capitalize())

# Swap case
print(myStr.swapcase())

# Get Length
print(len(myStr))

# Replace - **must all chars matches
print(myStr.replace('World', 'Everyone'))

# Count
sub = 'l'
print(myStr.count(sub))

# Starts with
print(myStr.startswith('hello')) # returns True

# Ends With
print(myStr.endswith('World')) # returns True

# Split to list
print(myStr.split())

# Find
print(myStr.find('e'))

# Index
print(myStr.index('e')) # same as find funciton but if failed to find it will through an Error

# Is all alphanumeric
print(myStr.isalnum())

# Is all alphabetic
print(myStr.isalpha())

# Is all numeric
print(myStr.isnumeric())