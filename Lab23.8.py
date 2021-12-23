import math

user_input = input()

my_list = []

while user_input != '*':
    my_list.append(user_input)
    user_input = input()

my_list = list(map(int, my_list))

my_list_reversed = my_list[::-1]

for x in my_list_reversed:
    print('{},'.format(x), end='')
print()





