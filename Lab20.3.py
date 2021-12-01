import math

people_attending = 7

slices_per_person = 2
slices_needed = people_attending * slices_per_person
#print(slices_needed)

slices_per_pizza = 12

pizzas_needed = math.ceil(slices_needed / slices_per_pizza)
print('Pizzas: {}'.format(pizzas_needed))

cost_per_pizza = 14.95
calc_cost = pizzas_needed * cost_per_pizza
print('Cost: ${:.2f}'.format(calc_cost))
