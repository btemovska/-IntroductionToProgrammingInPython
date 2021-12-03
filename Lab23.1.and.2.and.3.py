#Lab 23.1
my_text = input()
count = ''

for x in my_text:
    if x.isalpha():
        count = count + x
    if x.__contains__('?'):
        count = count + x
#print(count)
print(len(count))


# Lab 23.2
my_int = int(input())
char = ''

while 11 <= my_int <= 100:
    if my_int == 11:
        print(my_int)
        break
    print(my_int)
    my_int = my_int - 1
    char = str(my_int)
    if char[0] == char[1]:
        print(char)
        break
else:
    print('Input must be 11-100')


#Lab 23.3
my_int = int(input())
my_list = []

while my_int > 0:
    my_list.append(my_int)
    my_int = int(input())

print('{} and {}'.format(min(my_list), max(my_list)))