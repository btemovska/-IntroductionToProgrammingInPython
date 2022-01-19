#example 1
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

#example 2
listA = ["M", "na", "i", "Ke"]
listB = ["y", "me", "s", "lly"]
for i, j in zip(listA, listB):
    list_C = i + j
    print(list_C, end=' ')
print()
#My name is Kelly


#example 3
import math
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers_squared = []
for x in numbers:
    x_squared = math.pow(x, 2)
    numbers_squared.append(math.floor(x_squared))
print(numbers_squared)

#example 4
list3 = ["Hello ", "take "]
list4 = ["Dear", "Sir"]
final_list = []
for x in list3:
    for y in list4:
        final_list.append(x + y)
print(final_list)


#example 5
list5 = [10, 20, 30, 40]
list6 = [100, 200, 300, 400]
for x, y in zip(list5, list6[::-1]):
    print(x, y)
print()
#OR
my_dict = dict(zip(list5, list6[::-1]))
for x, y in my_dict.items():
    print(x, y)

#example 6
list7 = [5, 20, 15, 20, 25, 50, 20]
for x in list7:
    if x == 20:
        list7.remove(x)
print(list7)