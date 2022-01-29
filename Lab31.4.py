"""Given an integer representing a 10-digit phone number,
output the area code, prefix, and line number using the format (800) 555-1212.
"""

phone_number = int(input())

''' Type your code here. '''

area_code = str(phone_number)[:3]
first_three = str(phone_number)[3:6]
last_three = str(phone_number)[-4:]

print('({}) {}-{}'.format(area_code, first_three, last_three))