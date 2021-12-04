integers_entered = input()

x = integers_entered.split(',')
#print(x)

a = int(x[0])
b = int(x[1])
c = int(x[2])

result = a + b - c
print(result)