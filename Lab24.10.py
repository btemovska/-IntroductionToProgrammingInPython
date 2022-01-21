def calc_toll(hour, is_morning, is_weekend):
    # Type your code here.
    price = 0.0
    if hour in range(1,7) and is_morning == True and is_weekend == False:
        price = 1.15
    if hour in range(7, 10) and is_morning == True and is_weekend == False:
        price = 2.95
    if hour in range(10, 12) and is_morning == True and is_weekend == False:
        price = 1.90
    if hour in range(1, 3) and is_morning == False and is_weekend == False:
        price = 1.90
    if hour in range(3, 8) and is_morning == False and is_weekend == False:
        price = 3.95
    if hour in range(8, 12) and is_morning == False and is_weekend == False:
        price = 1.40

    if hour in range(1, 7) and is_morning == True and is_weekend == True:
        price = 1.05
    if hour in range(8, 12) and is_morning == True and is_weekend == True:
        price = 2.15
    if hour in range(1, 8) and is_morning == False and is_weekend == True:
        price = 2.15
    if hour in range(8, 12) and is_morning == False and is_weekend == True:
        price = 1.1
    return price

if __name__ == '__main__':
    print(calc_toll(8, True, False))
    print(calc_toll(1, False, False))
    print(calc_toll(3, False, True))
    print(calc_toll(5, True, True))



