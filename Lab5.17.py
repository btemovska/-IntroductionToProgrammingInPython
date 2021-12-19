''' Type your code here. '''
list = (3, 4, 5)

par_input = int(input())
num_strokes_input = int(input())

x = par_input - num_strokes_input

if x == 1 and par_input in list:
    print('Birdie')
if x == 2 and par_input in list:
    print('Eagle')
if x == 0 and par_input in list:
    print('Par')
if x < 0 and par_input in list:
    print('Bogey')
if x < 0 and par_input not in list:
    print('Error')




