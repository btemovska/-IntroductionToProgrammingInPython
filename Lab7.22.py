def swap_values(user_val1, user_val2):
    return '{1} {0}'.format(user_val1, user_val2)


if __name__ == '__main__':
    num_1 = int(input())
    num_2 = int(input())

    print(swap_values(num_1, num_2))
