"""Write a program that first reads in the name of an input file and
then reads the file using the csv.reader() method. The file contains a list of
words separated by commas. Your program should output the words and their frequencies
(the number of times each word appears in the file) without any duplicates.

"""

import csv

# Type your code here.
file_name = input()

with open(file_name, 'r') as file_name:
    user_list = csv.reader(file_name)
    list1 = []
    for x in user_list:
        for y in x:
            list1.append(y)

distinct_list = []

for z in list1:
    if z not in distinct_list:
        distinct_list.append(z)


for h in distinct_list:
    if h in list1:
        print('{} {}'.format(h, list1.count(h)))