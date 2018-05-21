# Open of file
fo = open('test.txt', 'w')

# Get some info
print('Name: ', fo.name)
print('Is Closed: ', fo.closed)
print('Open Mode: ', fo.mode)

fo.write('I love Python')
fo.write(' and Javascript')
fo.close()

# Open to append
fo = open('test.txt', 'a')
fo.write(' and also like PHP')
fo.close()

# Read from file
fo = open('test.txt', 'r+')
text = fo.read(10)
print(text)
fo.close()

# Create a file
fo = open('test2.txt', 'w+')
fo.write('This is my new file')
fo.close()

# File Permissions
# w -> write and replace the file if exists
# w+ -> write and Create a file if not exists
# r+ -> read from file
# a -> append will the changes to the end