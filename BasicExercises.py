#EX1
#Write a program to accept a string from the user
# and display characters that are present at an even index number.
str = "pynative"

for x in str:
    if str.index(x) % 2 == 0:
        print(x)

#EX 2
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

if numbers_x[0] == numbers_x[-1]:
    print(True)
else:
    print(False)

if numbers_y[0] == numbers_y[-1]:
    print(True)
else:
    print(False)

#EX 3
given_list = [10, 20, 33, 46, 55]
for x in given_list:
    if x % 5 == 0:
        print(x)

#EX 4
str_x = "Emma is good developer. Emma is a writer"
print(str_x.count("Emma"))

#EX 5
orig_num = "125"
if orig_num == orig_num[::-1]:
    print('Palindrome')
else:
    print('not palindrome')

#EX 6
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

odd_list = []
even_list = []

for x in list1:
    if x % 2 != 0:
        odd_list.append(x)
for y in list2:
    if y % 2 == 0:
        even_list.append(y)

final_list = odd_list + even_list
print(final_list)

