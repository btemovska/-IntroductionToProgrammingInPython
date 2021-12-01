import math

a = float(int(input))
b = float(int(input))

# c^2 = a^2 + b^2

c = math.pow(a, 2) + math.pow(b, 2)
c = math.sqrt(c)
#print(c)

print('Hypotenuse: {:.2f}'.format(c))




