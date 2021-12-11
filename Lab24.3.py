# Define your function here
def seconds_to_jiffies(user_seconds):
    jiffies = user_seconds * 100
    return jiffies

if __name__ == '__main__':
    # Type your code here. Your code must call the function.
    user_seconds_entered = int(input())
    print('{:.2f}'.format(seconds_to_jiffies(user_seconds_entered)))





