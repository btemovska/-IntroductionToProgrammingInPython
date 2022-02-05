def get_month_as_int(monthString):

    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int


user_string = input()
my_list = []

while user_string != '-1':
    my_list.append(user_string)
    user_string = input()


my_new_list = []
for x in my_list:
    if x.__contains__(','):
        my_new_list.append(x)

list1 = []
year_list = []
month_list = []
day_list = []

for x in my_new_list:
    first_space = x.find(' ')
    month = x[0:first_space]
    month_list.append(month)
    year = x[-4:]
    year_list.append(year)
    find_comma = x.find(',')
    date = x[first_space+1:find_comma]
    day_list.append(date)

month_list_numb = []
for x in month_list:
    month_numb = get_month_as_int(x)
    month_list_numb.append(month_numb)

if len(month_list_numb) == 5:
    print('{}/{}/{}'.format(month_list_numb[0], day_list[0], year_list[0]))
    print('{}/{}/{}'.format(month_list_numb[1], day_list[1], year_list[1]))
    print('{}/{}/{}'.format(month_list_numb[2], day_list[2], year_list[2]))
    print('{}/{}/{}'.format(month_list_numb[3], day_list[3], year_list[3]))
    print('{}/{}/{}'.format(month_list_numb[4], day_list[4], year_list[4]))
if len(month_list_numb) == 4:
    print('{}/{}/{}'.format(month_list_numb[0], day_list[0], year_list[0]))
    print('{}/{}/{}'.format(month_list_numb[1], day_list[1], year_list[1]))
    print('{}/{}/{}'.format(month_list_numb[2], day_list[2], year_list[2]))
    print('{}/{}/{}'.format(month_list_numb[3], day_list[3], year_list[3]))
if len(month_list_numb) == 3:
    print('{}/{}/{}'.format(month_list_numb[0], day_list[0], year_list[0]))
    print('{}/{}/{}'.format(month_list_numb[1], day_list[1], year_list[1]))
    print('{}/{}/{}'.format(month_list_numb[2], day_list[2], year_list[2]))
if len(month_list_numb) == 2:
    print('{}/{}/{}'.format(month_list_numb[0], day_list[0], year_list[0]))
    print('{}/{}/{}'.format(month_list_numb[1], day_list[1], year_list[1]))
if len(month_list_numb) == 1:
    print('{}/{}/{}'.format(month_list_numb[0], day_list[0], year_list[0]))

#OR
def get_month_as_int(monthString):

    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int


user_string = input()

list1 = []
list2 = []

while user_string != '-1':
    list1.append(user_string)
    user_string = input()

for x in list1:
    if x.__contains__(','):
        list2.append(x)

for y in list2:
    first_space_index = y.find(' ')
    month = y[:first_space_index]
    comma_index = y.find(',')
    day = y[first_space_index + 1 : comma_index]
    year = y[-4:]
    print(f'{get_month_as_int(month)}/{day}/{year}')

