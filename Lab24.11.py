#this needs re-done as the test are failing

def largest_number(num1, num2, num3):
    # Type your code here.
    largest_list = []
    largest_list.append(num1)
    largest_list.append(num2)
    largest_list.append(num3)
    sorted_list = sorted(largest_list)
    num = sorted_list[-1]
    print('largest: ', end='')
    print(num)


def smallest_number(num1, num2, num3):
    #Type your code here.
    smallest_list = []
    smallest_list.append(num1)
    smallest_list.append(num2)
    smallest_list.append(num3)
    sorted_list = sorted(smallest_list)
    num_a = sorted_list[0]
    print('smallest: ', end='')
    print(num_a)


if __name__ == '__main__':
    # Type your code here.
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    largest_number(num1, num2, num3)
    smallest_number(num1, num2, num3)

