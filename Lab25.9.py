user_entered = input()
user_entered_list = user_entered.split()
#print(user_entered_list)

x = user_entered_list[1][0:5]
#print(x)
y = user_entered_list[0][0]
#print(y)
z = user_entered_list[2][-2:]
#print(z)

print('Your login name: {}{}{}'.format(x, y, z))



