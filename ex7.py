def edit_distance(s1,s2):
    '''(str,str) -> int
    Takes in two words of the same
    length and tells the number
    of changes it would take
    s1 to make s2
    '''
    # base case, no letters left
    if (s1 == ''):
        # do nothing
        result = 0
    # if we still have letters
    else:
        # check if letters are not the same
        if (s1[0] != s2[0]):
            # add one to the distance, get rid of first letter
            result = 1 + edit_distance(s1[1:],s2[1:])
        # if they're the same, just try again
        else:
            # dont add anything, recurse again
            result = edit_distance(s1[1:],s2[1:])
    # send that result home
    return result

def subsequence(s1,s2):
    '''(str,str) -> bool
    Takes in two words and tells
    the user if the second word
    contains the first word
    '''
    # base case first word is empty
    if (s1 == ''):
        # it contains it
        result = True
    # second base case, went through second word
    elif (s2 == ''):
        # it doesnt contain it
        result = False
    # if we havent gotten all the letters
    else:
        # if the letters in both are the same
        if (s1[0] == s2[0]):
            # get rid of that same letter
            result = subsequence(s1[1:],s2[1:])
        # if theyre not the same
        else:
            # just slice the second words letter
            result = subsequence(s1,s2[1:])
    # send that value home
    return result

def perms(s):
    '''(str) -> set of str
    Takes in a string and returns all the
    possible permutations of that string
    '''
    # instatiate result
    result = set()
    # base case, if were down to one letter
    if len(s) == 1:
        # add the regular word
        result.add(s)
    # if we're still going through letters
    else:
        # go through each letter in the word
        for i in s:
            # go through every possibility of other letters
            for j in perms(s[:s.index(i)] + s[s.index(i) +1:]):
                # add the permutation to the set
                result.add(i + j)
    # return the set of words
    return result
        