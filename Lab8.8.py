#Lab 8.8
string_entered = input()

while string_entered != 'quit 0':
    integer = string_entered.split(" ", 1)[1]
#print(integer)

    phrase = string_entered.split(" ", 1)[0]
#print(phrase)
    print('Eating {} {} a day keeps the doctor away.'.format(integer, phrase))
    string_entered = input()

#much better way
user_entered = input()

space_index = user_entered.find(' ') #6
user_word = user_entered[0:space_index]
user_digit = user_entered[space_index+1:]

while user_word != 'quit':
    print(f'Eating {user_digit} {user_word} a day keeps the doctor away.')
    user_entered = input()
    space_index = user_entered.find(' ')
    user_word = user_entered[0:space_index]
    user_digit = user_entered[space_index+1:]
