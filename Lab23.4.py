num_of_integers = int(input())
list = []

for i in range(0, num_of_integers):
    i = int(input())
    list.append(i)
threshold = int(input())

list_two = []

for x in list:
    if x <= threshold:
        print(x, end=',')


