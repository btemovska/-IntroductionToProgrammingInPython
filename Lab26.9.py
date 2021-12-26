# Define your get_user_values function here
def get_user_values(nums):
    pass

# Define your output_ints_less_than_or_equal_to_threshold function here
def output_ints_less_than_or_equal_to_threshold(nums, threshold):
    for x in nums:
        if x <= threshold:
            print(x)


if __name__ == '__main__':
    threshold = int(input())
    nums = []

    user_nums = int(input())

    while user_nums != -1:
        nums.append(user_nums)
        user_nums = int(input())

    get_user_values(nums)
    output_ints_less_than_or_equal_to_threshold(nums, threshold)