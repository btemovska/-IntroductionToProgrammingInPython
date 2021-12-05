
my_input = input()

character = my_input[0]
#print(character)

phrase = my_input[2:]
#print(phrase)

list = []

for x in phrase:
    if x == character:
        #print(x)
        list.append(x)

print(len(list))
