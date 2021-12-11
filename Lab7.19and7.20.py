#Lab7.19
# Define your function here.
def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    return driven_miles * (1.0/miles_per_gallon) * dollars_per_gallon

if __name__ == '__main__':
    # Type your code here.
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())

    miles_10 = driving_cost(10, miles_per_gallon, dollars_per_gallon)
    miles_50 = driving_cost(50, miles_per_gallon, dollars_per_gallon)
    miles_400 = driving_cost(400, miles_per_gallon, dollars_per_gallon)

    print('{:.2f}'.format(miles_10))
    print('{:.2f}'.format(miles_50))
    print('{:.2f}'.format(miles_400))


#Lab7.20
# Define your function here
def feet_to_steps(user_feet):
    one_step_in_feet = 2.5
    num_steps_walked = user_feet / one_step_in_feet
    return int(num_steps_walked)

if __name__ == '__main__':
    # Type your code here
    num_feet_walked_entered = float(input())
    #print('{:.0f}'.format(feet_to_steps(num_feet_walked_entered)))
    print(feet_to_steps(num_feet_walked_entered))