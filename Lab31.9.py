"""A pedometer treats walking 2,000 steps as walking 1 mile.
Write a steps_to_miles() function that takes the number of steps
as a parameter and returns the miles walked. The steps_to_miles()
function throws a ValueError object with the message
"Exception: Negative step count entered." when the number of steps is negative.
Complete the main() program that reads the number of steps from a user,
calls the steps_to_miles() function, and outputs the returned value from the
steps_to_miles() function. Use a try-except block to catch any ValueError object
thrown by the steps_to_miles() function and output the exception message.
"""

# Define your method here
def steps_to_miles(num_steps):
    if num_steps < 0:
        raise ValueError('Exception: Negative step count entered.')
    else:
        return num_steps / 2000


if __name__ == '__main__':
    # Type your code here.
    user_steps = int(input())

    try:
        print('{:.2f}'.format(steps_to_miles(user_steps)))
    except ValueError as err:
        print(err)