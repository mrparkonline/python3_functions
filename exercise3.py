# U6E3 - Exercise Set 3 Solutions
# Mr Park

'''
- Fibonacci Calculator
- Random Integer List Generator
'''

def average(array):
    ''' average() calculates the average the given list

    --param
    array : list

    --return
    float
    '''

    if array:
        return sum(array) / len(array)
    else:
        return 0.0
# end of average

def factors(num):
    ''' factors() calculates the factors of a number and puts them in a list

    --param
    num : integer

    --return
    list
    '''

    if num < 1:
        return []
    elif num == 1:
        return [1]
    else:
        result = []
        for n in range(1,num+1):
            if num % n == 0:
                result.append(n)

        return result
# end of factors

def fib(n):
    ''' fib() calculates the nth Fibonacci number

    We will only deal with natural numbers >= 0

    --param
    n : integer

    --returns
    integer
    '''

    if n in [0,1]:
        return n
    else:
        fib_0 = 0
        fib_1 = 1
        fib_n = 0 # initialization

        for i in range(2,n+1):
            fib_n = fib_0 + fib_1
            fib_0 = fib_1
            fib_1 = fib_n

        return fib_n
# end of fib

def randList(lower, upper, size):
    ''' randList returns a list of random integers from lower to upper set bounds
    the list will have size many values ... list is element of [lower, upper)


    -- param
    lower : integer
    upper : integer
    size : integer

    -- return
    list
    '''

    if size == 0:
        return []
    elif lower > upper:
        return []
    elif lower == upper:
        return [lower] * size
    else:
        from random import randrange

        result = []
        for c in range(size):
            result.append(randrange(lower,upper))

        return result
# end of randList
