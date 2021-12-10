# not my code - followed instructor
category = []
name = []
description = []
available = []

input_filename = input()
f = open(input_filename)

for row in f:
    fields = row[:-1].split('\t')
    category.append(fields[0])
    name.append(fields[1])
    description.append(fields[2])
    available.append(fields[3])

for rowNum in range(len(available)):
    if available[rowNum] == "Available":
        print('{} ({}) -- {}'.format(name[rowNum], category[rowNum], description[rowNum]))



