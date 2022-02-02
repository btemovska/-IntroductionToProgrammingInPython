"""Write a program to calculate the total price for car wash services.
A base car wash is $10. A dictionary with each additional service and
the corresponding cost has been provided. Two additional services can be selected.
A '-' signifies an additional service was not selected. Output all selected services,
according to the input order, along with the corresponding costs and then the total
price for all car wash services.

"""

def my_func(base_wash, list1):
    print('ZyCar Wash')
    print('Base car wash -- ${}'.format(base_wash))
    list2=[]
    for x in list1:
        if x in services.keys():
            print('{} -- ${}'.format(x, services.get(x)))
            list2.append(services.get(x))
    print('----')
    print('Total price: ${}'.format(base_wash + sum(list2)))

services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()

''' Type your code here '''
list1 = []
list1.append(service_choice1)
list1.append(service_choice2)

my_func(base_wash, list1)

