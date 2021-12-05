#count how many multiples of x are
# in the range of low and high
low = int(input())
high = int(input())
x = int(input())
list = []

for y in range(low, high + 1):
    if y % x == 0:
        #print(y)
        list.append(y)
#print(list)

print('{:.0f}'.format(len(list)))