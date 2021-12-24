# Define your function here
def is_list_even(my_list):
    x_list = []
    for x in my_list:
        if x % 2 == 0:
            x_list.append('even')
        else:
            x_list.append('odd')
    if x_list.__contains__('odd'):
        z = 'neither'
    else:
        z = 'all even'
    return z

def is_list_odd(my_list):
    x_list = []
    for x in my_list:
        if x % 2 != 0:
            x_list.append('odd')
        else:
            x_list.append('even')
    if x_list.__contains__('even'):
        z = 'neither'
    else:
        z = 'all odd'
    return z


if __name__ == '__main__':
    # Type your code here.
    num_integers = int(input())
    my_list = []

    for x in range(num_integers):
        user_number = int(input())
        my_list.append(user_number)

    even = is_list_even(my_list)
    odd = is_list_odd(my_list)

    if even == 'neither' and odd == 'neither':
        print('not even or odd')
    if even == 'neither' and odd == 'all odd':
        print('all odd')
    if even == 'all even' and odd == 'neither':
        print('all even')