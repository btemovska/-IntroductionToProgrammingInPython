lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))

print()

print('Lemonade ingredients - yields {:.2f} servings'.format(servings))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice_cups))
print('{:.2f} cup(s) water'.format(water))
print('{:.2f} cup(s) agave nectar'.format(agave_nectar))

print()

new_servings = int(input('How many servings would you like to make?\n'))

print()

print('Lemonade ingredients - yields {:.2f} servings'.format(new_servings))
x = float(new_servings / servings) #8
print('{:.2f} cup(s) lemon juice'.format(x * lemon_juice_cups))
print('{:.2f} cup(s) water'.format(x * water))
print('{:.2f} cup(s) agave nectar'.format(x * agave_nectar))

print()
print('Lemonade ingredients - yields {:.2f} servings'.format(new_servings))
gallon_lemon = (x * lemon_juice_cups) / 16
print('{:.2f} gallon(s) lemon juice'.format(gallon_lemon))
gallon_water = (x * water) / 16
print('{:.2f} gallon(s) water'.format(gallon_water))
gallon_agave = (x * agave_nectar) / 16
print('{:.2f} gallon(s) agave nectar'.format(gallon_agave))


