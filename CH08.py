#LAB 8.5
user_string = '42,000'
if user_string.isdigit() == True:
    print('yes')
else:
    print('no')

#LAB 8.6
user_input = 'Michael Jordan'
my_list = user_input.split(' ')

if len(my_list) == 2:
    output = my_list[1] + ', ' + my_list[0][0] + '.'
    print(output)
if len(my_list) == 3:
    output = my_list[2] + ', ' + my_list[0][0] + '.' + my_list[1][0] + '.'
    print(output)
