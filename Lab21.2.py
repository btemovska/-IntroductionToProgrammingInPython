import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
x = wall_height * wall_width
print('Wall area: {} square feet'.format(x))

# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
y = round((x / 350),2)
print('Paint needed: {} gallons'.format(y))

# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
z = math.ceil(y)
print('Cans needed: {} can(s)'.format(z))

# FIXME (4): Calculate and output the total cost of paint can needed depending on color
print()
color_chosen = input('Choose a color to paint the wall:\n')
price_color = ''
if color_chosen in paint_colors.keys():
    price_color = paint_colors.get(color_chosen)
    print('Cost of purchasing {} paint: ${}'.format(color_chosen,(price_color * z)))




