def get_user_values(my_list):
    return my_list

def output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    for x in user_values:
        if x <= upper_threshold:
            print(x)
    # return value


if __name__ == '__main__':
    num_integers = int(input())
    my_list = []

    for x in range(num_integers):
        user_numbers = int(input())
        my_list.append(user_numbers)

    threshold = int(input())

    get_user_values(my_list)
    output_ints_less_than_or_equal_to_threshold(my_list, threshold)



