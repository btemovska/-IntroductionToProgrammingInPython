large_pizza_cost = 9.99
num_pizzas = int(input())

tax = 0.06

subtotal = num_pizzas * large_pizza_cost
#print(subtotal)
x = subtotal * tax
#print(x)
total = x + subtotal
#print(total)

print('Subtotal: ${:.2f}'.format(subtotal))
print('Total due: ${:.2f}'.format(total))









