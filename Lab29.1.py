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


# my code finally
# Type your code here
file_name = input()

with open(file_name, 'r') as f:
    foods_list = f.readlines()

    for x in foods_list:
        if x.__contains__('Available'):
            #print(x.strip())
            first_tab = x.find('\t')
            category = x[:first_tab]
            second_tab = (x[first_tab + 1 :].find('\t')) + first_tab
            item = x[first_tab + 1 : second_tab + 1]
            available_index = x.find('Available')
            desc = x[second_tab +2 : available_index - 1]

            print(f'{item} ({category}) -- {desc}')
       
