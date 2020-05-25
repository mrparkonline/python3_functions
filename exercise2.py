# U6E2 - Exercise Set 2 Solutions
# Mr Park

def removeSpace(word):
    ''' removeSpace removes all whitespaces in a string

    --param
    word : string

    --returns
    string
    '''

    return word.replace(' ','')
# end of removeSpace

def duplicates(sequence):
    ''' duplicates returns a list of values that occur more than once

    --param
    sequence : list or string

    --returns
    list
    '''

    result = []

    for item in sequence:
        if item not in result and sequence.count(item) >= 2:
            result.append(item)

    return result
# end of duplicates

def search(sequence, target):
    ''' search looks for the first occurance of the target in the sequence

    --param
    sequence : list or string
    target : any data type

    --returns
    integer
    '''

    # We will be implementing an algorithm called Linear Search
    # Link: https://en.wikipedia.org/wiki/Linear_search
    if not sequence:
        return -1
    else:
        for i in range(len(sequence)):
            if sequence[i] == target:
                return i
        else:
            return -1
# end of search

def intersect(array1, array2):
    ''' intersect looks for values in both list arguments and returns only those
    values in a list

    --param
    array1 : list
    array2 : list

    --returns
    list
    '''

    if not array1 or not array2:
        # If any of the list is empty, we return an empty list
        return []
    else:
        result = [] # initialization

        for item in array1:
            if item not in result and item in array2:
                result.append(item)

        return result
# end of intersect
