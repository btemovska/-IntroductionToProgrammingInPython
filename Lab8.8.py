
string_entered = input()

while string_entered != 'quit 0':
    integer = string_entered.split(" ", 1)[1]
#print(integer)

    phrase = string_entered.split(" ", 1)[0]
#print(phrase)
    print('Eating {} {} a day keeps the doctor away.'.format(integer, phrase))
    string_entered = input()


