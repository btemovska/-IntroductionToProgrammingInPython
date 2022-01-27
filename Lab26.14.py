# FIXME (1): Prompt for four weights. Add all weights to a list. Output list.

# FIXME (2): Output average of weights.

# FIXME (3): Output max weight from list.

# FIXME (4): Prompt the user for a list index and output that weight in pounds and kilograms.

# FIXME (5): Sort the list and output it.

weight_1 = float(input('Enter weight 1:\n'))
weight_2 = float(input('Enter weight 2:\n'))
weight_3 = float(input('Enter weight 3:\n'))
weight_4 = float(input('Enter weight 4:\n'))


weight_list = []
weight_list.append(weight_1)
weight_list.append(weight_2)
weight_list.append(weight_3)
weight_list.append(weight_4)

print('Weights: {}'.format(weight_list))

print('\nAverage weight: {:.2f}'.format(sum(weight_list)/len(weight_list)))
print('Max weight: {:.2f}\n'.format(max(weight_list)))

list_location = int(input('Enter a list location (1 - 4):\n'))
list_location -= 1
print('Weight in pounds: {:.2f}'.format(weight_list[list_location]))
print('Weight in kilograms: {:.2f}'.format(weight_list[list_location] / 2.2))
weight_list.sort()
print('\nSorted list: {}'.format(weight_list))