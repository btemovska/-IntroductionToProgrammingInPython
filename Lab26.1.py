list_integers = input().split()

new_list = []
for x in list_integers:
    new_list.append(x)

new_list_a = list(map(int, new_list))


middle = int(len(new_list_a)/2)
#print(middle)


if len(new_list_a) <= 9:
    print(new_list_a[middle])
else:
    print('Too many inputs')

