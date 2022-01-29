"""Driving is expensive. Write a program with a car's miles/gallon
and gas dollars/gallon (both floats) as input, and output the
gas cost for 20 miles, 75 miles, and 500 miles."""


miles_per_gallon = float(input())
gas_dollars_per_gallon = float(input())

x = (20 / miles_per_gallon) * gas_dollars_per_gallon
y = (75 / miles_per_gallon) * gas_dollars_per_gallon
z = (500 / miles_per_gallon) * gas_dollars_per_gallon

print('{:.2f} {:.2f} {:.2f}'.format(x, y, z))