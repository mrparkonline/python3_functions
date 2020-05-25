# U6E1 - Exercise Set 1 Solution
# Mr Park

'''
note:
- To use any of these functions, you can import the file and try calling the
functions
'''

def isEven(num):
    ''' isEven determines if the given argument is an even number

    --param
    num : integer

    --return
    boolean
    '''

    return num % 2 == 0
# end of isEven

def isPalindrome(word):
    ''' isPalindrome determines if the given argument is a palindrome

    For this solution, we will assume that there are no whitespaces and special
    characters

    --param
    word : string

    --return
    boolean
    '''

    word = word.lower()

    return word == word[::-1]
# end of isPalindrome

def isPrime(num):
    ''' isPrime determines if the given argument integer is a prime number

    --param
    num : integer

    --return
    boolean
    '''

    if num < 2:
        return False
    elif num in [2,3]:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False # return acts like a break
                # as soon as it finds a factor, it will exit the function
                # and return False
        else:
            return True
# end of isPrime

def vowelCounter(word):
    ''' vowelCounter returns the number of vowels in a string

    --param
    word : string

    --return
    integer
    '''

    if word:
        counter = 0
        for character in word.lower():
            if character in 'aeiou':
                counter += 1

        return counter
    else:
        # empty string
        return 0
# end of vowelCounter

def factorial(num):
    ''' factorial() is the ! mathematical operator

    --param
    num : integer

    --return
    integer
    '''

    if num < 1:
        return -1 # -1 is more of an error code ...
    elif num in [0,1]:
        return 1
    else:
        result = 1
        for i in range(1,num+1):
            result *= i

        return result
# end of factorial
