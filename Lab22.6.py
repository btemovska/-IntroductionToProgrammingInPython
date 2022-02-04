# Type your code here
print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

print()

services = {'Oil change': '35','Tire rotation': '19','Car wash': '7', 'Car wax': '12'}

first_service = input('Select first service:\n')
second_service = input('Select second service:\n')

print()

print('Davy\'s auto shop invoice')
print()
if first_service in services.keys():
    print('Service 1: {}, ${}'.format(first_service, services.get(first_service)))
    cost_first = int(services.get(first_service))
else:
    print('Service 1: No service')
    cost_first = 0
if second_service in services.keys():
    print('Service 2: {}, ${}'.format(second_service, services.get(second_service)))
    cost_second = int(services.get(second_service))
else:
    print('Service 2: No service')
    cost_second = 0

print()

total = cost_first + cost_second
print('Total: ${}'.format(total))



#--better code---

# Type your code here
services = {'Oil change':35, 'Tire rotation':19, 'Car wash':7, 'Car wax':12}

print('Davy\'s auto shop services')
for x, y in services.items():
    print('{} -- ${}'.format(x, y))

first_service = input('\nSelect first service:\n')
second_service = input('Select second service:\n')

print('\nDavy\'s auto shop invoice')

my_list = []
my_list.append(first_service)
my_list.append(second_service)
service_num = 1
list_two = []
print()

for x in my_list:
    if x in services.keys():
        print(f'Service {service_num}: {x}, ${services.get(x)}')
        list_two.append(services.get(x))
    else:
        print(f'Service {service_num}: No service')

    service_num +=1

print(f'\nTotal: ${sum(list_two)}')