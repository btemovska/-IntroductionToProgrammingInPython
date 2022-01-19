import math
user_weight = int(input('Please enter your weight:\n'))
y = input('(L)bs or (K)g:\n').lower()

if y == 'k':
    kilo = 2.22  # 2.22 pounds in a kilo
    print('You are {} pounds'.format(math.ceil(user_weight * kilo)))
else:
    pound = 0.454  #0.454 kilo in pounds
    print('You are {} kilos'.format(math.ceil(user_weight * pound)))




