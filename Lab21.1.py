fav_color = input('Enter favorite color:\n')
pet_name = input('Enter pet\'s name:\n')
number = int(input('Enter a number:\n'))

print('You entered: {} {} {}'.format(fav_color, pet_name, number))

first_password = fav_color + "_" + pet_name
second_password = str(number) + fav_color + str(number)

print()

print('First password: {}'.format(first_password))
print('Second password: {}'.format(second_password))

print()

print('Number of characters in {}: {}'.format(first_password, len(first_password)))
print('Number of characters in {}: {}'.format(second_password, len(second_password)))

