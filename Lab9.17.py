''' Type your code here. '''
user_list = input().split()
user_list = list(map(int, user_list))

positive_int = []

for x in user_list:
    if x >= 0:
        positive_int.append(x)

positive_int.sort()

for x in positive_int:
    print(x, end = ' ')


