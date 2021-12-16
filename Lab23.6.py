numbers = int(input())
my_list = []

while numbers >= 0:
    my_list.append(numbers)
    numbers = int(input())


#print(my_list)

for x in my_list:
    x = max(my_list)

print(x)