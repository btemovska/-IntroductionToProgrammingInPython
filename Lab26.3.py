user_list = input().split()

old_word_list = []
new_word_list = []
for x, y in enumerate(user_list):
    if x % 2 == 0:
        old_word_list.append(y)
    else:
        new_word_list.append(y)

my_dict = dict(zip(old_word_list, new_word_list))

user_sentence_list = input().split()

for x in user_sentence_list:
    if x in my_dict.keys():
        replacement_word = x.replace(x, my_dict.get(x))
        # if replacement_word
        if replacement_word == user_sentence_list[-1]:
            print(replacement_word, end='')
        else:
            print(replacement_word, end=' ')
    else:
        replacement_word = x
        if replacement_word == user_sentence_list[-1]:
            print(replacement_word, end='')
        else:
            print(replacement_word, end=' ')

print()


#OR
''' Type your code here. '''
user_words_list = input().rstrip().split()
user_sentence_list = input().rstrip().split()

old_words = []
new_words = []

for x , y in enumerate(user_words_list):
    if x % 2 == 0:
        old_words.append(y)
    else:
        new_words.append(y)

my_dict = dict(zip(old_words, new_words))

sentence = ''

for z in user_sentence_list:
    if z in my_dict.keys():
        sentence = sentence + " " + my_dict.get(z)
    else:
        sentence = sentence + " " + z

sentence = sentence.lstrip()
print(sentence)
