#19.2
user_num = int(input('Enter integer:\n'))

num_one = user_num

print('You entered: {}'.format(num_one))
num_one_squared = num_one * num_one
print('{} squared is {}'.format(num_one, num_one_squared))
num_one_cubed = num_one * num_one * num_one
print('And {} cubed is {}'.format(num_one, num_one_cubed), '!!')

user_num_two = int(input('Enter another integer:\n'))

num_two = user_num_two

adding = num_one + num_two
print('{} + {} is {}'.format(num_one, num_two, adding))
adding = num_one * num_two
print('{} * {} is {}'.format(num_one, num_two, adding))

#19.3
# Draw tree
print('   *')
print('  ***')
print(' *****')
print('*******')
print('  ***')

print()
print()
print('/\   /\\')
print('  o o')
print(' =   =')
print('  ---')
