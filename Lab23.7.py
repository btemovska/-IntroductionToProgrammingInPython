''' Type your code here. '''
import math
n = 25
integer = 0

my_list = []
my_list.append(math.floor(n))

while n >= 2:
    if n % 2 == 0:
        n = n / 2
        my_list.append(math.floor(n))
    elif n % 2 != 0:
        n = n * 3 + 1
        my_list.append(math.floor(n))
    integer += 1

for x, char in enumerate(my_list):
    print(char, end='\t')
    if x == 9:
        print()
    if x == 19:
        print()
    if x == len(my_list)-1:
        str(char).split('\t')
        print()
#NO IDEA how to eliminate the tab in the last index