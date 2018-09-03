def greeting(name):
    ''' (str) -> str
    Returns a personalized greeting to the
    person whose name was given
    >>> greeting("Dan")
    "Hello Dan how are you today?"
    '''
    # return the personalized greeting
    return "Hello " + name + " how are you today?"

def mutate_list(my_list):
    ''' (list) -> NoneType
    Mutates a list so all ints are multiplied by 2,
    all booleans are inverted, all strings have first
    and last characters removed, and the 0th element
    is always changed to "Hello"
    >>> list = [2,True,'john',2]
    >>> mutate_list(list)
    >>> print(list)
    ["Hello",False,'oh',4]
    '''
    # go through the list
    for i in range (0,len(my_list)):
        # first element needs to be "Hello"
        if (i==0):
            # change first element to "Hello"
            my_list[i]= "Hello"
        # see if we have an int
        elif (type(my_list[i]) == int):
            # multiply by two
            my_list[i] = my_list[i]*2
        # see if we have boolean
        elif (type(my_list[i]) == bool):
            # invert it using not
            my_list[i] = not my_list[i]
        # see if we have string
        elif (type(my_list[i]) == str):
            # remove first and last characters with indexing
            my_list[i] = my_list[i][1:len(my_list[i])-1]
            
def merge_dicts(d1,d2):
    ''' (dict,dict) -> dict
    Takes two different dicts and returns a new dict
    that is the result of both previous dicts merged together
    >>> d1 = {'a': [1, 2, 3], 'b': [4], 'c': [5, 6, 7]}
    >>> d2 = {'a': [2], 'b': [8, 9, 0], 'd': [10, 11, 12]}
    >>> merge_dicts(d1, d2)
    {'a': [1, 2, 3, 2], 'b': [4, 8, 9, 0], 'c': [5, 6, 7], 'd': [10, 11, 12]}
    >>> merge_dicts(d2, d1)
    {'a': [2, 1, 2, 3], 'b': [8, 9, 0, 4], 'c': [5, 6, 7], 'd': [10, 11, 12]}
    '''
    # get lists of each of the keys
    keys1 = list(d1.keys())
    keys2 = list(d2.keys())
    # make a blank dict
    d3 = {}
    # go through all keys in one of the dicts
    for i in keys1:
        # check if the key is in the other dict
        if (i in keys2):
            # add the lists
            d3[i] = d1[i]+d2[i]
            # delete it from the list
            keys2.remove(i)
        # if it is in the first and not the last
        else:
            # just make it equal
            d3[i] = d1[i]
        # account for the remaining keys in d2, go through remaining
        for i in keys2:
            # make them equal
            d3[i] = d2[i]
    # return finished, merged product
    return d3