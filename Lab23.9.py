triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')

for x in range(0, triangle_height):
    for y in range(0, x + 1):
        print(triangle_char, end=' ')
    print()




