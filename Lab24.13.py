def get_num_of_characters(input_str):
    # Type your code here
    count = 0
    for x in input_str:
        count = count + 1
    return count

def output_without_whitespace(input_str):
    input_str = input_str.replace(' ', '')
    return input_str


if __name__ == '__main__':
    # Type your code here
    user_sentence = input('Enter a sentence or phrase:\n')
    print('\nYou entered: {}'.format(user_sentence))

    print('\nNumber of characters: {}'.format(get_num_of_characters(user_sentence)))
    print('String with no whitespace: {}'.format(output_without_whitespace(user_sentence)))
