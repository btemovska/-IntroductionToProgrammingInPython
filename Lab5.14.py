highway_num = 1000

if highway_num == 0 or highway_num == 200:
    print('{} is not a valid interstate highway number.'.format(highway_num))
elif highway_num >= 1 and highway_num <= 99:
    if highway_num % 2 == 0:
        print('I-{} is primary, going east/west.'.format(highway_num))
    else:
        print('I-{} is primary, going north/south.'.format(highway_num))
elif highway_num >= 100 and highway_num <= 999:
    if highway_num % 2 == 0:
        if str(highway_num)[1] == '0':
            print('I-{} is auxiliary, serving I-{}, going east/west.'.format(highway_num, str(highway_num)[-1:]))
        else:
            print('I-{} is auxiliary, serving I-{}, going east/west.'.format(highway_num, str(highway_num)[-2:]))
    else:
        if str(highway_num)[1] == '0':
            print('I-{} is auxiliary, serving I-{}, going north/south.'.format(highway_num, str(highway_num)[-1:]))
        else:
            print('I-{} is auxiliary, serving I-{}, going north/south.'.format(highway_num, str(highway_num)[-2:]))
else:
    print('{} is not a valid interstate highway number.'.format(highway_num))
