names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

# Type your code here.

try:
    x = names[index]
    print('Name: {}'.format(x))
except:
    print('Exception! list index out of range')
    if index >= len(names):
        print('The closest name is: {}'.format(names[-1]))
    else:
        print('The closest name is: {}'.format(names[0]))