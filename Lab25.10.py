user_string = input('Enter input string:\n')
first_word = ''
second_word = ''
my_list = []

while user_string != 'q':
    if user_string.__contains__(','):
        my_list = user_string.split(',')
        first_word = my_list[0].strip()
        second_word = my_list[1].strip()
        print('First word: {}'.format(first_word))
        print('Second word: {}'.format(second_word))

        user_string = input('\nEnter input string:\n')
    else:
        print('Error: No comma in string.')

        user_string = input('\nEnter input string:\n')
