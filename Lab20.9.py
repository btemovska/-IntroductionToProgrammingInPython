user_int = int(input('Enter integer (32 - 126):\n'))

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
user_float = float(input('Enter float:\n'))
user_char = input('Enter character:\n')
user_string = input('Enter string:\n')
print('{} {} {} {}'.format(user_int, user_float, user_char, user_string))

# FIXME (2): Output the four values in reverse
print('{} {} {} {}'.format(user_string, user_char, user_float, user_int))

# FIXME (3): Convert the integer to a characer, and output that character
y = chr(user_int)
print('{} converted to a character is {}'.format(user_int, y))