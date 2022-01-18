''' Type your code here. '''
user_nums = input().split()
user_nums = list(map(int, user_nums))

avg_num = sum(user_nums)/len(user_nums)
max_num = max(user_nums)

print('{:.0f} {:.0f}'.format(avg_num, max_num))