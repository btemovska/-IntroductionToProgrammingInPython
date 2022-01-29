"""Given four values representing counts of quarters, dimes, nickels and pennies,
output the total amount as dollars and cents."""

quarters = int(input())
dimes = int(input())
nickles = int(input())
pennies = int(input())

dollars = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)

print(f'Amount: ${dollars:.2f}')