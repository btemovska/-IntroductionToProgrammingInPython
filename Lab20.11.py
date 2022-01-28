food_name_1 = input('Enter food item name:\n')
food_price_1 = float(input('Enter item price:\n'))
item_qty_1 = int(input('Enter item quantity:\n'))

total_1 = item_qty_1 * food_price_1
print('\nRECEIPT')
print('{} {} @ ${:.2f} = ${:.2f}'.format(item_qty_1, food_name_1, food_price_1, total_1))
print('Total cost: ${:.2f}'.format(total_1))

food_name_2 = input('\n\nEnter second food item name:\n')
food_price_2 = float(input('Enter item price:\n'))
item_qty_2 = int(input('Enter item quantity:\n'))

total_2 = item_qty_2 * food_price_2
print('\nRECEIPT')
print('{} {} @ ${:.2f} = ${:.2f}'.format(item_qty_1, food_name_1, food_price_1, total_1))
print('{} {} @ ${:.2f} = ${:.2f}'.format(item_qty_2, food_name_2, food_price_2, total_2))
final_total = total_1 + total_2
print('Total cost: ${:.2f}'.format(final_total))

qratuity_perc = 0.15
gratuity_dollars = final_total * qratuity_perc
print('\n15% gratuity: ${:.2f}'.format(gratuity_dollars))
print('Total with tip: ${:.2f}'.format(final_total + gratuity_dollars))

