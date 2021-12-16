# Define your function here
my_list = []
def count_evens(num1, num2, num3, num4):
    my_list.append(num1)
    my_list.append(num2)
    my_list.append(num3)
    my_list.append(num4)

    new_list = []
    for x in my_list:
        if x % 2 == 0:
            #print('even')
            new_list.append(x)
        else:
            pass

    return len(new_list)


if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())

    result = count_evens(num1, num2, num3, num4)
    print('Total evens:', result)



