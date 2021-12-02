red = int(input())
green = int(input())
blue = int(input())

list = []
list.append(red)
list.append(green)
list.append(blue)
#print(list)

gray = min(list)
#print(gray)

red = red - gray
green = green - gray
blue = blue - gray

print('{} {} {}'.format(red, green, blue))


