#LAB 9.16
user_input = input()
new_list = user_input.split(' ')
#print(new_list) #['15', '20', '0', '5']

integer_map = map(int, new_list)
integer_list = list(integer_map)
#print(integer_list) #[15, 20, 0, 5]

sum = sum(integer_list)

average = sum / len(integer_list)
print('{:.0f}'.format(average), end=' ')

maximum = max(integer_list)
print('{:.0f}'.format(maximum))


#LAB 9.17
user_input = input() #3 99 3 0 27
new_list = user_input.split(' ')

integer_map = map(int, new_list)
integer_list = list(integer_map)

integer_list.sort()

for n in integer_list:
    if n >= 0:
        print(n, '', end='')
#0 3 3 27 99


