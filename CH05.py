#5.4.5: exercise
year = int(input())

if year >= 2101:
    print('Distant future')
elif year >= 2001:
    print('21st century')
elif year >= 1901:
    print('20th century')
else:
    print('Long ago')


# 5.14 LAB
highway_number = 5
a = 'I-' + str(highway_number)

a_string = str(highway_number)
a_length = len(a_string)
c = int(a_string[a_length - 2: a_length])
c2 = str(c)
concatenate_C = 'I-' + c2 + ','
concatenate_D = 'I-' + c2

if(highway_number == 200):
    print(highway_number, 'is not a valid interstate highway number.')
elif ((highway_number % 2) == 0 and (highway_number >= 1 and highway_number <= 99)):
    print(a, 'is primary, going east/west.')
elif (highway_number >= 1 and highway_number <= 99):
    print(concatenate_D, 'is primary, going north/south.')
elif(highway_number % 2) == 0 and (highway_number >= 100 and highway_number <= 999):
    print(a, 'is auxiliary, serving', concatenate_C , 'going east/west.')
elif(highway_number >= 100 and highway_number <= 999):
    print(a, 'is auxiliary, serving', concatenate_C , 'going north/south.')
else:
    print(highway_number, 'is not a valid interstate highway number.')

# 5.15 LAB
input_month = 'February'
input_day = 31

if (input_month == 'March') and (input_day >= 20 and input_day <= 31):
    print('Spring')
elif (input_month == 'April') and (input_day >= 1 and input_day <= 30):
    print('Spring')
elif (input_month == 'May') and (input_day >= 1 and input_day <= 31):
    print('Spring')
elif (input_month == 'June') and (input_day >=1  and input_day <= 20):
    print('Spring')

elif (input_month == 'June') and (input_day >= 21 and input_day <= 30):
    print('Summer')
elif (input_month == 'July') and (input_day >= 1 and input_day <= 31):
    print('Summer')
elif (input_month == 'August') and (input_day >= 1 and input_day <= 31):
    print('Summer')
elif (input_month == 'September') and (input_day >=1  and input_day <= 21):
    print('Summer')

elif (input_month == 'September') and (input_day >= 22 and input_day <= 30):
    print('Autumn')
elif (input_month == 'October') and (input_day >= 1 and input_day <= 31):
    print('Autumn')
elif (input_month == 'November') and (input_day >= 1 and input_day <= 30):
    print('Autumn')
elif (input_month == 'December') and (input_day >=1  and input_day <= 20):
    print('Autumn')

elif (input_month == 'December') and (input_day >= 21 and input_day <= 31):
    print('Winter')
elif (input_month == 'January') and (input_day >= 1 and input_day <= 31):
    print('Winter')
elif (input_month == 'February') and (input_day >= 1 and input_day <= 29):
    print('Winter')
elif (input_month == 'March') and (input_day >=1  and input_day <= 19):
    print('Winter')

else:
    print('Invalid')

# #5.16 LAB - note need to figure out how to exclude 1900
# input_year = int(input())
# c_1 = input_year / 4
# c_2 = input_year / 400
#
# if (c_1 - int(c_1) == 0) and (c_2 - int(c_2) == 0):
#     print("{} - leap year".format(input_year))
# elif c_1 - int(c_1) == 0:
#     print("{} - leap year".format(input_year))
# else:
#     print("{} - not a leap year".format(input_year))

# 5.15 Lab
is_leap_year = False
input_year = int(input())
''' Type your code here. '''
x = ((input_year % 4 == 0) and (input_year % 100 != 0 or input_year % 400 == 0))
if x == True:
    print('{} - leap year'.format(input_year))
else:
    print('{} - not a leap year'.format(input_year))