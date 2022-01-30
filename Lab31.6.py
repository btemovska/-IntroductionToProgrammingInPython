"""Write a program with total change amount as an integer input,
and output the change using the fewest coins, one coin type per line.
The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies.
Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.
"""
''' Type your code here. '''
import math

x_dollars = 0
x_quarters = 0
x_dimes = 0
x_nickles = 0
x_pennies = 0
x_remainder = 0

money_entered = int(input())

if money_entered <= 0:
    print('No change')
else:
    x_dollars = money_entered // 100 #1
    if x_dollars == 1:
        print(x_dollars, 'Dollar')
    elif x_dollars == 0:
        pass
    else:
        print(x_dollars, 'Dollars')

    x_remainder = money_entered - (x_dollars * 100)

    x_quarters = x_remainder // 25
    if x_quarters == 1:
        print(x_quarters, 'Quarter')
    elif x_quarters == 0:
        pass
    else:
        print(x_quarters, 'Quarters')

    x_remainder = x_remainder - (x_quarters * 25)

    x_dimes = x_remainder // 10
    if x_dimes == 1:
        print(x_dimes, 'Dime')
    elif x_dimes == 0:
        pass
    else:
        print(x_dimes, 'Dimes')

    x_remainder = x_remainder - (x_dimes * 10)

    x_nickles = x_remainder // 5
    if x_nickles == 1:
        print(x_nickles, 'Nickel')
    elif x_nickles == 0:
        pass
    else:
        print(x_nickles, 'Nickels')

    x_remainder = x_remainder - (x_nickles * 5)

    x_pennies = x_remainder // 1
    if x_pennies == 1:
        print(x_pennies, 'Penny')
    elif x_pennies == 0:
        pass
    else:
        print(x_pennies, 'Pennies')
