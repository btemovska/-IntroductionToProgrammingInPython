#3.12 LAB
#import math

user_num = int(input())
x = int(input())

num1 = user_num / x
num2 = num1 / x
num3 = num2 / x

print(int(num1), int(num2), int(num3))

#3.13 LAB
''' Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184 '''
''' Men: Calories = ((Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184 '''

''' Type your code here. '''

age = int(input())
weight = int(input())
heart_rate = int(input())
time = int(input())

calories_women = ((age * 0.074) - (weight * 0.05741) + (heart_rate * 0.4472) - 20.4022) * time / 4.184
calories_man = ((age * 0.2017) + (weight * 0.09036) + (heart_rate * 0.6309) - 55.0969) * time / 4.184

print('Women: {:.2f} calories'.format(calories_women))
print('Men: {:.2f} calories'.format(calories_man))

#3.14 LAB
import math
x = float(input())
y = float(input())
z = float(input())

your_value1 = math.pow(x, z)
your_value2 = math.pow(x, math.pow(y, z))
your_value3 = math.fabs(x - y)
your_value4 = math.sqrt(math.pow(x, z))

print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3, your_value4))