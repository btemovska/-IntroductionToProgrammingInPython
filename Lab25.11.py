data_title = input('Enter a title for the data:\n')
print('You entered: {}'.format(data_title))

column_1 = input('\nEnter the column 1 header:\n')
print('You entered: {}'.format(column_1))

column_2 = input('\nEnter the column 2 header:\n')
print('You entered: {}'.format(column_2))

data_points = input('\nEnter a data point (-1 to stop input):\n')
data_points_list = []
data_string_list = []
data_int_list = []
count_commas = 0

while data_points != '-1':
    count_commas = data_points.count(',')
    if count_commas == 1:
        try:
            data_points_list = data_points.split(',')
            data_string = data_points_list[0].strip()
            data_int = int(data_points_list[1].strip())

            data_string_list.append(data_string)
            data_int_list.append(data_int)

            print('Data string: {}'.format(data_string))
            print('Data integer: {}'.format(data_int))

            data_points = input('\nEnter a data point (-1 to stop input):\n')

        except ValueError as err:
            print('Error: Comma not followed by an integer.')
            data_points = input('\nEnter a data point (-1 to stop input):\n')

    elif count_commas == 0:
        print('Error: No comma in string.')
        data_points = input('\nEnter a data point (-1 to stop input):\n')
    elif count_commas > 1:
        print('Error: Too many commas in input.')
        data_points = input('\nEnter a data point (-1 to stop input):\n')

print()
print('{:>33}'.format(data_title))
print('{:<20}|{:>23}'.format(column_1, column_2))
print('--------------------------------------------')
my_dict = dict(zip(data_string_list, data_int_list))
for x, y in my_dict.items():
    print('{:<20}|{:>23}'.format(x, y))
print()

for x, y in my_dict.items():
    print('{:>20} {}'.format(x, ('*'* y)))