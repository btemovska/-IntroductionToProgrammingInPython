def get_age():
    age = int(input())
    # TODO: Raise exception for invalid ages
    if age >= 18 and age <= 75:
        return age
    raise ValueError('Invalid age.\nCould not calculate heart rate info.')

    # return age


# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * 0.70
    return 'Fat burning heart rate for a {} year-old: {} bpm'.format(age, heart_rate)


if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        print(fat_burning_heart_rate(age))
    except ValueError as x:
        print(x)

