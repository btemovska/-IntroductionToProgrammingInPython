"""
(1) Prompt the user to enter a string of their choosing. Output the string. (1 pt)
(2) Complete the get_num_of_characters() function, which returns the number of characters
in the user's string. We encourage you to use a for loop in this function. (2 pts)
(3) Extend the program by calling the get_num_of_characters() function and
then output the returned result. (1 pt)
(4) Extend the program further by implementing the output_without_whitespace()
function. output_without_whitespace() outputs the string's characters except
for whitespace (spaces, tabs). Note: A tab is '\t'. Call the output_without_whitespace()
function in main(). (2 pts)
"""

def get_num_of_characters(user_string):
    # Type your code here
    return len(user_string)


if __name__ == '__main__':
    # Type your code here
    user_string = input('Enter a sentence or phrase:\n')

    print('\nYou entered: {}'.format(user_string))

    print('\nNumber of characters: {}'.format(get_num_of_characters(user_string)))
    print('String with no whitespace: {}'.format(user_string.replace(" ", "")))