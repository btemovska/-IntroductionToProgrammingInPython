# The words parameter is a list of strings.
def build_dictionary(words):
    # The frequencies dictionary will be built with your code below.
    # Each key is a word string and the corresponding value is an integer
    # indicating that word's frequency.

    ''' Type your code here (remove the "pass" statement below) '''
    list_1 = []
    for x in words:
        if x not in list_1:
            list_1.append(x)

    list_2 = []
    for y in list_1:
        num = words.count(y)
        list_2.append(num)

    my_dict = dict(zip(list_1, list_2))

    return my_dict
    #pass

# The following code asks for input, splits the input into a word list,
# calls build_dictionary(), and displays the contents sorted by key.
if __name__ == '__main__':
    words = input().split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ': ' + str(your_dictionary[key]))

    #print(build_dictionary(words))