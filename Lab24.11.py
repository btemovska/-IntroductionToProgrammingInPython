def largest_number(num1, num2, num3):
    # Type your code here.
    largest_number = max(num1, num2, num3)
    return largest_number

def smallest_number(num1, num2, num3):
    # Type your code here.
    smallest_number = min(num1, num2, num3)
    return smallest_number


if __name__ == '__main__':
    # Type your code here.
    int1 = int(input())
    int2 = int(input())
    int3 = int(input())

    print('largest: {}'.format(largest_number(int1, int2, int3)))
    print('smallest: {}'.format(smallest_number(int1, int2, int3)))