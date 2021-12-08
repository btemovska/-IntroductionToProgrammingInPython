
def integer_to_reverse_binary(integer_value):
    x = bin(integer_value)
    y = x[2:]
    return y


def reverse_string(input_string):
    a = bin(input_string)
    b = a[2:]
    z = b[::-1]
    return z

if __name__ == '__main__':
    user_entered = int(input())

    print(integer_to_reverse_binary(user_entered))
    print(reverse_string(user_entered))


# x = 6
# x_bin = bin(x)
# print(x_bin)
# x_bin = x_bin[2:]
# print(x_bin)
# x_bin_reversed = x_bin[::-1]
# print(x_bin_reversed)