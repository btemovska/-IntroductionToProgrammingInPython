print('Task1')
#TASK 1
# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
    # Student code goes here
    index = x
    print(mystring[0:index])

# expected output: WGU
printFirst('WGU College of IT', 3)

# expected output: WGU College
printFirst('WGU College of IT', 11)

print('Task2')
#TASK 2
# Complete the function to return the last X number of characters
# in the given string
def getLast(mystring, x):
    # Student code goes here
    index = x
    return (mystring[-index:])

# expected output: IT
print(getLast('WGU College of IT', 2))

# expected output: College of IT
print(getLast('WGU College of IT', 13))

print('Task3')
#TASK 3
# Complete the function to return True if the word WGU exists in the given string
# otherwise return False
def containsWGU(mystring):
    # Student code goes here
    if mystring.__contains__('WGU'):
        return True
    else:
        return False

# expected output: True
print(containsWGU('WGU College of IT'))

# expected output: False
print(containsWGU('Night Owls Rock'))

print('Task4')
#TASK 4
# Complete the function to print all of the words in the given string
def printWords(mystring):
    # Student code goes here
    my_list = mystring.split()
    print(my_list)

# expected output: ['WGU', 'College', 'of', 'IT']
printWords('WGU College of IT')

# expected output: ['Night', 'Owls', 'Rock']
printWords('Night Owls Rock')

print('Task5')
#TASK 5
# Complete the function to combine the words into a sentence and return a string
def combineWords(words):
    # Student code goes here
    for x in words:
        print(x, end=' ')
    print()

# expected output: WGU College of IT
combineWords(['WGU', 'College', 'of', 'IT'])

# expected output: Night Owls Rock
combineWords(['Night', 'Owls', 'Rock'])

print('Task6')
#TASK 6
# Complete the function to replace the word WGU with Western Governors University
# and print the new string
def replaceWGU(mystring):
    # Student code goes here
    my_string = mystring.replace("WGU", 'Western Governors University')
    print(my_string)

# expected output: Western Governors University Rocks
replaceWGU('WGU Rocks')

# expected output: Hello, Western Governors University
replaceWGU('Hello, WGU')

print('Task7')
#TASK 7
# Complete the function to remove the word WGU from the given string
# ONLY if it's not the first word and return the new string
def removeWGU(mystring):
    # Student code goes here
    my_list = mystring.split()
    word = 'WGU'
    for x in my_list:
        if x == 'WGU' and x == my_list[0]:
            return mystring
        else:
            my_new_string = mystring.replace("WGU", '')
            return my_new_string

# expected output: WGU Rocks
print(removeWGU('WGU Rocks'))

# expected output: Hello, John
print(removeWGU('Hello, WGUJohn'))

print('Task9')
#TASK 9
# Complete the function to print the specified hourly rate with two decimals
def displayHourlyRate(rate):
    # Student code goes here
    print('${:.2f}'.format(rate))

# expected output: $34.79
displayHourlyRate(34.789123)

# expected output: $24.12
displayHourlyRate(24.123456)

print('Task 10')
#TASK 10
# Complete the function to return the number of uppercase letters in the given string
def countUpper(mystring):
    # Student code goes here
    count = 0
    for x in mystring:
        if x.isupper():
            count = count + 1
    return count

# expected output: 4
print(countUpper('Welcome to WGU'))

# expected output: 2
print(countUpper('Hello, Mary'))

print('TASK 8')
#TASK 8
# Complete the function to remove trailing spaces from the first string
# and leading spaces from the second string and return the combined strings
def removeSpaces(string1, string2):
    # Student code goes here
    string1 = string1.strip()
    string2 = string2.strip()
    print('{}{}'.format(string1, string2))

# expected output: WGU Rocks-You know it!
removeSpaces('WGU Rocks    ', '  -You know it!')

# expected output: Welcome WGU-IT Students
removeSpaces('Welcome WGU ', ' -IT Students')