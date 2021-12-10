service = input('Enter desired auto service:\n')

services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7}

if service in services.keys():
    print('You entered: {}'.format(service))
    print('Cost of {}: ${}'.format(service.lower(), services.get(service)))
else:
    print('You entered: {}'.format(service))
    print('Error: Requested service is not recognized')

