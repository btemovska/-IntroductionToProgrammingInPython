my_char = input()
my_list = input()
user_list = my_list.split()
#print(user_list) #['hello', 'zoo', 'sleep', 'drizzle']

for x in user_list:
    if x.__contains__(my_char) == True:
        my_word = x
        print(my_word)

