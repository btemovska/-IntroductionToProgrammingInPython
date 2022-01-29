"""A palindrome is a word or a phrase that is the same when read
both forward and backward. Examples are: "bob," "sees," or
"never odd or even" (ignoring spaces). Write a program whose
input is a word or phrase, and that outputs whether the input is a palindrome.
"""

user_word = input()

user_word2 = user_word.replace(" ", "")
if user_word2 == user_word2[::-1]:
    print('{} is a palindrome'.format(user_word))
else:
    print('{} is not a palindrome'.format(user_word))


