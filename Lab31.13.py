"""Write a program that takes in a line of text as input,
and outputs that line of text in reverse. The program repeats,
ending when the user enters "Done", "done", or "d" for the line of text.

"""

''' Type your code here. '''
user_text = input()

list1 = ["Done", "done", "d" ]
list2 = []

while user_text not in list1:
    list2.append(user_text)
    user_text = input()

for x in list2:
    print(x[::-1])