user_list = input().split()
user_list = list(map(int, user_list))

threshold = user_list[-1]

for x in user_list:
    if x < threshold:
        print('{},'.format(x), end ='')
print()