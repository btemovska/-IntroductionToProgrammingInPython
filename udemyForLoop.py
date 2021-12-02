# find all uppercases
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
upper_case = ''

for x in quote:
    if x.isupper():
        upper_case = upper_case + x

print(upper_case) #ASMEWPOIRFWSPHR



#write a program to print out all numbers from 0 to 9
for x in range(0, 10):
    print(x)


#write a program to print out all numbers from 0 to 100
#    that is divisible by 7

for y in range(0, 101):
    if y % 7 == 0:
        print(y)




