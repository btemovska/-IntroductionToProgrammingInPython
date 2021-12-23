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