my_dict = {}
user_entered = input() #Joe 123-5432 Linda 983-4123 Frank 867-5309
user_entered = user_entered.split()

names = [] #creating list just for names
numbers = [] #creating list just for numbers

for x in user_entered:
    if x.isalpha():
        names.append(x)
    else:
        numbers.append(x)

my_dict = dict(zip(names, numbers)) #this creates the dict

number_to_get = input() #ask for name in the dict (Linda)
phone_number = ''

if number_to_get in my_dict.keys():
    phone_number = my_dict.get(number_to_get)

print(phone_number) #983-4123

