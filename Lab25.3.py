def check_character(word, index):
    #x = word[index]
    if word[index].isalpha():
        y = """Character '{}' is a letter""".format(word[index])
    elif word[index].isspace():
        y = """Character '{}' is a white space""".format(word[index])
    elif word[index].isdigit():
        y = """Character '{}' is a digit""".format(word[index])
    else:
        y = """Character '{}' is unknown""".format(word[index])
    return y

if __name__ == '__main__':
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))



