#4.12 LAB
caffeine_mg = float(input())

your_value = caffeine_mg / 2
your_value2 = your_value / 2
your_value3 = your_value2 / 4

print('After 6 hours: {:.2f}'.format(your_value), 'mg')
print('After 12 hours: {:.2f}'.format(your_value2), 'mg')
print('After 24 hours: {:.2f}'.format(your_value3), 'mg')

#4.13 LAB
current_price = int(input())
last_months_price = int(input())

change_LM = current_price - last_months_price
est_mortgage = (current_price * 0.051) / 12

print('This house is ${}. The change is ${} since last month.'.format(current_price, change_LM))
print('The estimated monthly mortgage is ${:.2f}.'.format(est_mortgage))

#4.14 LAB
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

product = num1 * num2 * num3 * num4
avg = (num1 + num2 + num3 + num4) / 4

print('{:.0f} {:.0f}'.format(product, avg))
print('{:.3f} {:.3f}'.format(product, avg))