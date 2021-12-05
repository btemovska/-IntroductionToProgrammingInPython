numbers_entered = input()
lower_and_upper = input()

lower = lower_and_upper.split(' ')[0]
upper = lower_and_upper.split(' ')[1]
lower = int(lower)
upper = int(upper)
#print(lower) #0
#print(upper) #50

numbers_entered_split = numbers_entered.split(' ')
#print(numbers_entered_split)
#note this creates list


#converting string list into int list
numbers_entered_split = list(map(int, numbers_entered_split))
#print(numbers_entered_split)

for y in numbers_entered_split:
    if y >= lower and y <= upper:
        print(y, end=' ')
