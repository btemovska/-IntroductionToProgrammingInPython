def get_age():
    age = int(input())
    if age >=18 and age <=75:
        return age
    raise ValueError("Invalid age.\nCould not calculate heart rate info.")
    # TODO: Raise exception for invalid ages
    #return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    x = 220 - age
    heart_rate = x * 0.70
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age, heart_rate))
    except ValueError as x:
        print(x)
