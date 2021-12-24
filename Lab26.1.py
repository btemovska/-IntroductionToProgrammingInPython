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


#better
user_list = input()

my_list = user_list.split()
my_list = list(map(int, my_list))

if len(my_list) <= 9:
    #the code goeshere
    middle = len(my_list) // 2
    print(my_list[middle])

else:
    print('Too many inputs')

