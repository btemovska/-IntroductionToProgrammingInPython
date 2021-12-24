import math

''' Type your code here. '''
radius = float(input())
height = float(input())

pi = math.pi

volumeformula = pi*(math.pow(radius, 2))*height
areaformula = (2 * pi * radius * height) + (2 * pi * (math.pow(radius, 2)))

print('Volume: {:.1f} cubic inches'.format(volumeformula))
print('Surface area: {:.1f} square inches'.format(areaformula))
