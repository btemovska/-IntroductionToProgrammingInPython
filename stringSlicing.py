number = "9,364,557,576,534,247,576"
print(number[1::4]) #,,,,,,

alphabet = 'abcdefghijklmnopqrstuvwxyz'
backwards = alphabet[25:0:-1]
backwards2 = alphabet[25::-1]
backwards3 = alphabet[::-1]

print(backwards) #zyxwvutsrqponmlkjihgfedcb
print(backwards2) #zyxwvutsrqponmlkjihgfedcba
print(backwards3) #zyxwvutsrqponmlkjihgfedcba

#exercise
print(alphabet[16:13:-1]) #qpo
print(alphabet[4::-1]) #edcba
print(alphabet[:-9:-1]) #zyxwvuts
