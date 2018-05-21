# Loops

# For loops
people = ['Jon', 'Sara', 'Tim', 'Bob']
for person in people:
    print('Current Person: ', person)

# Iterate by seq index
for i in range(len(people)):
    print('Current Person: ', people[i])

for i in range(0, 10):
    print(i)

# While Loop
count = 0
while count <= 10:
    print('Count: ', count)
    count = count + 1

while count <= 10:
    print('Count: ', count)
    count = count + 1
    if count == 5:
        break