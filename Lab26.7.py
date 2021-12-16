def remove_evens(nums):
    # Type your code here.
    new_list = []
    for x in nums:
        if x % 2 == 0:
            pass
        else:
            new_list.append(x)
            y = new_list
    return y

if __name__ == '__main__':
    nums = [1, 9, 3]
    result = remove_evens(nums)

    print(result)



