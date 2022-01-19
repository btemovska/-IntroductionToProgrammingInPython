''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

#''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

#''' Type your code here. '''
x_val = 0
y_val = 0
final = ''

for x in range(-10, 10):
    for y in range(-10, 10):
        eq1 = (a * x) + (b * y)
        eq2 = (d * x) + (e * y)
        if eq1 == c and eq2 == f:
            final = 'found'
            x_val = x
            y_val = y

if final == 'found':
    print('x = {}, y = {}'.format(x_val, y_val))
else:
    print('There is no solution')