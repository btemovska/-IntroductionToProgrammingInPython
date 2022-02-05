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


#OR
user_string = input('Enter input string:\n').rstrip().replace(" ", "")

while user_string != 'q':
    if user_string.__contains__(','):

        first_comma_index = user_string.find(',')
        first_word = user_string[:first_comma_index]
        second_word = user_string[first_comma_index + 1:]

        print(f'First word: {first_word}')
        print(f'Second word: {second_word}')

        user_string = input('\nEnter input string:\n').rstrip().replace(" ", "")

    else:
        print('Error: No comma in string.')
        user_string = input('\nEnter input string:\n').rstrip().replace(" ", "")