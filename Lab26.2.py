list_of_words = input()

list_of_words = list_of_words.split()
print(list_of_words)

word = ''
y = 0
for x in list_of_words:
    print('{} {}'.format(x, list_of_words.count(x)))

