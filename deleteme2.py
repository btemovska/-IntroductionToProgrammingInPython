# Define your function here
def is_list_even(my_list):
    even_list = []
    for x in my_list:
        if x % 2 == 0:
            even_list.append('even')
    num_evens = even_list.count('even')
    if num_evens == len(my_list):
        return "all even"

def is_list_odd(my_list):
    odd_list = []
    for x in my_list:
        if x % 2 != 0:
            odd_list.append('odd')
    num_odd = odd_list.count('odd')
    if num_odd == len(my_list):
        return "all odd"

if __name__ == '__main__':
    # Type your code here.

    user_num = int(input())
    my_list = []

    while len(my_list) != user_num:
        user_num2 = int(input())
        my_list.append(user_num2)

    if is_list_even(my_list) == 'all even':
        print('all even')
    elif is_list_odd(my_list) == 'all odd':
        print('all odd')
    else:
        print('not even or odd')

