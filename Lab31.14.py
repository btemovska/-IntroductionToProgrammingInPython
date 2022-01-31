"""The Fibonacci sequence begins with 0 and then 1 follows.
All subsequent values are the sum of the previous two,
ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function,
which has an index n as parameter and returns the nth value in the sequence.
Any negative index values should return -1.

"""

def fibonacci(n):
    # Type your code here.
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
    return

if __name__ == '__main__':
    start_num = int(input())
    print('fibonacci({}) is {}'.format(start_num, fibonacci(start_num)))