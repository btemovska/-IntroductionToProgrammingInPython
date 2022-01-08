''' Type your code here. '''
count_of_quarters = int(input())
count_of_dimes = int(input())
count_of_nickles = int(input())
count_of_pennies = int(input())

one_quarter = 25
one_dime = 10
one_nicle = 5

dollar = one_quarter * count_of_quarters #100
dimes = one_dime * count_of_dimes #30
nicles = one_nicle * count_of_nickles #10

final = dollar + dimes + nicles + count_of_pennies

final2 = final /100

print(f'Amount: ${final2:.2f}')