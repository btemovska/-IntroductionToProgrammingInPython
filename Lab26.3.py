
x = input()
y = input()

x = x.split()
print(x)


if len(x) == 8:
    y = y.replace(x[0], x[1])
    y = y.replace(x[2], x[3])
    y = y.replace(x[4], x[5])
    y = y.replace(x[6], x[7])
    print(y)
elif len(x) == 6:
    y = y.replace(x[0], x[1])
    y = y.replace(x[2], x[3])
    y = y.replace(x[4], x[5])
    print(y)
elif len(x) == 4:
    y = y.replace(x[0], x[1])
    y = y.replace(x[2], x[3])
    print(y)
elif len(x) == 2:
    y = y.replace(x[0], x[1])
    print(y)
else:
    print('i don\'t know')

