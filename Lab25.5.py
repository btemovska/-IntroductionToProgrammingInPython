#extract middle 3 characters

my_string = input()

length = len(my_string)
#print('{} length'.format(length))
three_char = 3
x = length - three_char
#print(x)
y = int(x / 2)
#print(y)
word = my_string[y:-y]
#print(word)
# start = my_string[:y]
# print(start)
#
# my_string = not end

if length == 3:
    print('Midfix: {}'.format(my_string))
else:
    print('Midfix: {}'.format(word))


#OR
user_input = input().rstrip()

middle_index = len(user_input) // 2

print(f'Midfix: {user_input[middle_index - 1 : middle_index + 2]}')