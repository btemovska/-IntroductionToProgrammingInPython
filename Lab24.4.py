# Define your function here.
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    # Type your code here. Your code must call the function.
    year = int(input())

    if is_leap_year(year) is True:
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')