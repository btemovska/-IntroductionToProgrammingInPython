# TODO: Import the random module
import random

def number_guess(num):
    # TODO: Get a random number between 1-100
    x = random.randint(0, 100)
    x = x + 1

    # TODO: Read numbers and compare to random number
    #print(x)
    if x > num:
        print('{} is too low. Random number was {}.'.format(num, x))
    elif x < num:
        print('{} is too high. Random number was {}.'.format(num, x))
    else:
        print('{} is correct!'.format(num))

if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)

    # Convert the string tokens into integers
    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        number_guess(num)