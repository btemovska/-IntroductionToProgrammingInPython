def get_minimum_int(nums):
    #Type your code here.
    min_number = min(nums)
    return min_number


if __name__ == '__main__':
    #Type your code here.
    user_input = int(input())
    my_list = []

    while user_input != -1:
        my_list.append(user_input)
        user_input = int(input())

    list_a = []
    for x in my_list:
        z = x - get_minimum_int(my_list)
        # list_a.append(z)
        print(z)

    # print(list_a)
