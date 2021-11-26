#LAB 6.14
user_input = int(input())
user_input_bi = bin(user_input)[2:]
user_input_bi_reversed = user_input_bi[::-1]

while user_input > 0:
    print(user_input_bi_reversed)
    user_input = user_input - user_input

# LAB 6.15
word = 'mypassword'
password = ''

for x in word:
    if x == 'i':
        password += '1'
    elif x == 'a':
        password += '@'
    elif x == 'm':
        password += 'M'
    elif x == 'B':
        password += '8'
    elif x == 's':
        password += '$'
    else:
        password += x

password = password + '!'
print(password)

# LAB 6.16
a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

for x in range(-10, 11):
    for y in range(-10, 11):
        g = (a * x) + (b * y)
        h = (d * x) + (e * y)
        if (g == c) and (h == f):
            print("x = {}, y = {}".format(x, y))
else:
    print("There is no solution")

# LAB 6.17
a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

check = False

for x in range(-10, 11):
    for y in range(-10, 11):
        g = ((a * x) + (b * y))
        h = ((d * x) + (e * y))
        if (g == c) and (h == f):
            check = True
            x_solution = x
            y_solution = y
if check:
    print("x = {} , y = {}".format(x_solution, y_solution))
else:
    print("There is no solution")

# LAB 6.18
listA = []
n = int(input())

for i in range(0, n):
    i = float(input())
    listA.append(i)
    maximum_num = max(listA)

for x in listA:
    result = x / maximum_num
    print('{:.2f}'.format(result))

#user enters the total count of values
#user enters those values
#they are appended to a list
# the maximum value is calculated

#the second for goes through each value
#calcs results by dividing each value with the max
#prints the value for each

#Input
#5
# 30.0
# 50.0
# 10.0
# 100.0
# 65.0

#Output
# 0.30
# 0.50
# 0.10
# 1.00
# 0.65

