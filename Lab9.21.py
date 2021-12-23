#TASK 1
print("Task 1")
# Complete the function to return the first two items in the given list
def getFirstTwo(mylist):
    # Student code goes here
    list = []
    list.append(mylist[0])
    list.append(mylist[1])
    return list

# expected output: [8, 3]
print(getFirstTwo([8,3,5,2,10]))

# expected output: [15, 2]
print(getFirstTwo([15,2,10,12]))

#TASK 2
print("Task 2")
# Complete the function to return the last two items in the given list
def getLastTwo(mylist):
    # Student code goes here
    return mylist[-2:]

# expected output: [2, 10]
print(getLastTwo([8,3,5,2,10]))

# expected output: [9, 12]
print(getLastTwo([15,2,9,12]))

#TASK 3
print("Task 3")
# Complete the function to add num1 to the end of the given list
def addToEnd(mylist, num1):
    # Student code goes here
    mylist.append(num1)
    return mylist

# expected output: [4, 5, 6, 7]
print(addToEnd([4,5,6], 7))

# expected output: [9, 8, 7, 6]
print(addToEnd([9,8,7], 6))

#TASK 4
print("Task 4")
# Complete the function to add num1 to the front of the given list
def addToFront(mylist, num1):
    # Student code goes here
    mylist.insert(0, num1)
    return mylist

# expected output: [3, 4, 5, 6]
print(addToFront([4,5,6], 3))

# expected output: [10, 9, 8, 7]
print(addToFront([9,8,7], 10))

#TASK 5
print("Task 5")
# Complete the function to return a new list containing
# the first two and last two items in the given list
def getFirstTwoAndLastTwo(mylist):
    # Student code goes here
    my_new_list = []
    first_two = mylist[:2]
    last_two = mylist[-2:]
    my_new_list = first_two + last_two #unpacks list from nested list
    return my_new_list

# expected output: [8, 3, 19, 1]
print(getFirstTwoAndLastTwo([8,3,7,15,2,10,19,1]))

# expected output: [7, 15, 3, 5]
print(getFirstTwoAndLastTwo([7,15,2,10,19,1,3,5]))

#TASK 6
print("Task 6")
# Complete the function to remove the first item in the given list
def removeFirst(mylist):
    # Student code goes here
    mylist.remove(mylist[0])
    return mylist

# expected output: [7, 8, 9]
print(removeFirst([6,7,8,9]))

# expected output: [2, 3, 4]
print(removeFirst([1,2,3,4]))

#TASK 7
print("Task 7")
# Complete the function to remove the third item in the given list
def removeThird(mylist):
    # Student code goes here
    third_item = mylist[2]
    mylist.remove(third_item)
    return mylist

# expected output: [6, 7, 9]
print(removeThird([6,7,8,9]))

# expected output: [1, 2, 4]
print(removeThird([1,2,3,4]))

#TASK 8
print("Task 8")
# Complete the function to order the values in the list
# if ascending is true then order lowest to highest
# if ascending is false then order highest to lowest
def sortList(mylist, ascending):
    # Student code goes here
    if ascending == True:
        x = sorted(mylist)
    else:
        y = sorted(mylist)
        x = y[::-1]
    return x

# expected output: [4, 12, 19, 33]
print(sortList([19,4,33,12], True))

# expected output: [33, 19, 12, 4]
print(sortList([19,4,33,12], False))

#TASK 9
print("Task 9")
# Complete the function to return a dictionary using
# list1 as the keys and list2 as the values
def createDict(list1, list2):
    # Student code goes here
    my_dict = {}
    my_dict = dict(zip(list1, list2))
    return my_dict

# expected output: {'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}
print(createDict(['tomato', 'banana', 'lime'], ['red','yellow','green']))

# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(createDict(['Brazil', 'Ireland', 'Indonesia'], ['Brasilia','Dublin','Jakarta']))

