word = 'mypassword'
password = ''

my_dict = {'i': '1','a': '@','m': 'M','B': '8','s': '$'}

for x in word:
    if x in my_dict.keys():
        print(my_dict.get(x), end='')
    else:
        print(x, end='')
print('!')