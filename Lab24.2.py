import math

#Define your function here.
def max_magnitude(x, y):
    if (x and y) > 0:
        max_value = max(x, y)
    else:
        abs_x = math.fabs(x)
        abs_y = math.fabs(y)
        max_value = (math.ceil(max(abs_x, abs_y))) * (-1)
        # print('-{:.0f}'.format(max_value))
        # max_value = '-{:.0f}'.format(max_value)
    return max_value

if __name__ == '__main__':
    # Type your code here.
    num1 = int(input())
    num2 = int(input())
    print(max_magnitude(num1, num2))
