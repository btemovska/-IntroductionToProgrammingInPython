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

# TODO: Read dates from input, parse the dates to find the one
#       in the correct format, and output in m/d/yyyy format

list1 = []
while user_string != '-1':
    list1.append(user_string)
    user_string = input()

print(list1)
list2 = []

for x in list1:
    if x.__contains__(","):
        list2.append(x)

print(list2)

for x in list2:
    month = x[:x.find(" ")]
    day = x[(x.find(" ") + 1) : x.find(",")]
    year = x[-4:]
    print('{}/{}/{}'.format(get_month_as_int(month), day, year))


