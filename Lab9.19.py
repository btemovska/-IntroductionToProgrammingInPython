word_pairs = 'Mo 391-0993 Rachel 019-1265 Ruby 010-8712 Steve 312-3318 Maria 871-0091'
name_chosen = 'Rachel'

word_pairs = word_pairs.split(' ')
#print(word_pairs) #creates list

#print(len(word_pairs))
key_and_value_pairs = int(len(word_pairs) / 2)
#print(key_and_value_pairs)

my_dict = {}

if key_and_value_pairs == 1:
    my_dict[word_pairs[0]] = word_pairs[1]
elif key_and_value_pairs == 2:
    my_dict[word_pairs[0]] = word_pairs[1]
    my_dict[word_pairs[2]] = word_pairs[3]
elif key_and_value_pairs == 3:
    my_dict[word_pairs[0]] = word_pairs[1]
    my_dict[word_pairs[2]] = word_pairs[3]
    my_dict[word_pairs[4]] = word_pairs[5]
elif key_and_value_pairs == 4:
    my_dict[word_pairs[0]] = word_pairs[1]
    my_dict[word_pairs[2]] = word_pairs[3]
    my_dict[word_pairs[4]] = word_pairs[5]
    my_dict[word_pairs[6]] = word_pairs[7]
elif key_and_value_pairs == 5:
    my_dict[word_pairs[0]] = word_pairs[1]
    my_dict[word_pairs[2]] = word_pairs[3]
    my_dict[word_pairs[4]] = word_pairs[5]
    my_dict[word_pairs[6]] = word_pairs[7]
    my_dict[word_pairs[8]] = word_pairs[9]

#print(my_dict)

print(my_dict.get(name_chosen))