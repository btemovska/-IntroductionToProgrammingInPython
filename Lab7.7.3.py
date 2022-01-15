def print_shampoo_instructions(num_cycles):
    start = 1
    if num_cycles < 1:
        print('Too few')
    elif num_cycles > 4:
        print('Too many')
    else:
        while start <= num_cycles:
            print('{} : Lather and rinse.'.format(start))
            start += 1
    print('Done.')

user_cycles = int(input())
print_shampoo_instructions(user_cycles)