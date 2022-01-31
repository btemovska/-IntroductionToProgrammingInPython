"""Write a program whose input is two integers. Output the first integer
and subsequent increments of 5 as long as the value is less than or equal
to the second integer.
"""

''' Type your code here. '''
num1 = int(input())
num2 = int(input())

number = ''


if num2 < num1:
    print('Second integer can\'t be less than the first.')
else:
    while num1 <= num2:
        number = number + str(num1) + " "
        num1 += 5
    print(number)
