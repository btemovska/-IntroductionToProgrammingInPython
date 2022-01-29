#example 1
try:
    first_number = int(input('Enter first number:\n'))
    second_number = int(input('Enter second number:\n'))
    result = first_number / second_number
    print('Result: {:.0f}'.format(result))

except ZeroDivisionError:
    print('Can\'t devide by 0')
except ValueError:
    print('Invalid number')

#example 2