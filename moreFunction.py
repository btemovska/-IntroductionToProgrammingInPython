def split_check(tip, people, tax_percentage=0.09, tip_percentage=0.15):
    x = bill * tax_percentage
    y = bill * tip_percentage
    total_bill = (bill + x + y)/people

    return total_bill


bill = float(input())
people = int(input())
new_tax_percentage = float(input()) #optional
new_tip_percentage = float(input()) #optional

# Cost per diner at different tax and tip percentages
print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))

