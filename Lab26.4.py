tile_dict = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
             'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
             'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

''' Type your code here. '''
user_input = input().upper()

my_list = []
for x in user_input:
    #print(tile_dict.get(x))
    y = tile_dict.get(x)
    my_list.append(y)

#print(my_list)
print(sum(my_list))

#BETTER
tile_dict = { 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
              'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
              'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }

user_text = input()
sum = 0

for x in user_text:
    sum = sum + tile_dict.get(x)

print(sum)