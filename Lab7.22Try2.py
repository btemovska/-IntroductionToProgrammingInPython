# Define your function here.
def swap_values(user_val1, user_val2):
    #x = '{1} {0}'.format(user_val1, user_val2)
    return user_val2, user_val1

if __name__ == '__main__':
    # Type your code here. Your code must call the function.
    num_1 = int(input())
    num_2 = int(input())

    print(*swap_values(num_1, num_2))