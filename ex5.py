def rsum(my_list):
    '''(list of int) -> int
    Takes a list of integers and computes
    the sum of them recursively
    '''
    # if we've used all the values
    if (my_list == []):
        # base case, add nothing
        result = 0
    # if there are still values left
    else:
        # recursively add the next values
        result = my_list[0] + rsum(my_list[1:])
    # return result back to user
    return result


def rmax(my_list):
    '''(list of int) -> int
    Takes a list of integers and returns
    the highest integer in the list
    '''
    # if we only have one value left
    if (len(my_list) == 1):
        # return the remaining value
        result = my_list[0]
    # if we have more than one value to work with
    else:
        # check if current value is greater than the next
        if (my_list[0] > my_list[1]):
            # pop out the smaller value, retry
            result = rmax(my_list[0:1] + my_list[2:])
        # if the next value is higher
        else:
            # pop out the lower value, retry
            result = rmax(my_list[1:])
    # return the final result
    return result


def second_smallest(my_list):
    '''(list of int) -> int
    Takes a list of integers and returns
    the second smallest integer in the list
    '''
    # check if we only have the smallest value left
    if (len(my_list) == 2):
        # check if first is larger
        if (my_list[0] > my_list[1]):
            # result is the larger of lowest two
            result = my_list[0]
        # if the second is larger
        else:
            # result is largest of lowest two
            result = my_list[1]
    # if we have more than one left
    else:
        # check if next variable does not in bottom two
        if (my_list[2] > my_list[1] and my_list[2] > my_list[0]):
            # cut it out of the list, try again
            result = second_smallest(my_list[0:2] + my_list[3:])
        # check the second index doesnt belong in bottom two
        elif (my_list[1] > my_list[0]):
            # cut it out of the list, try again
            result = second_smallest(my_list[0:1] + my_list[2:])
        # check if the first index doesnt belong in bottom two
        else:
            # cut it out of the list, try again
            result = second_smallest(my_list[1:])
    # return the second lowest
    return result


def sum_max_min(my_list):
    '''(list of int) -> int
    Takes in a list of integers and returns the
    sum of the highest integer and lowest integer
    in the list
    '''
    print(my_list)
    # check if we only have the smallest value left
    if (len(my_list) == 2):
        # add them and return
        result = my_list[0] + my_list[1]
    # if we're not down to two yet
    else:
        # check if current value is between its surrounding values
        if ((my_list[1] > my_list[2] and my_list[1] < my_list[0]) or
                (my_list[1] < my_list[2] and my_list[1] > my_list[0])):
            # if its between, cut it out, not max or min
            result = sum_max_min(my_list[0:1] + my_list[2:])
        # check if its larger than the surrounding numbers
        elif (my_list[1] > my_list[2] and my_list[1] > my_list[0]):
            # check if 2nd value is smaller
            if (my_list[2] < my_list[0]):
                # remove the in between value
                result = sum_max_min(my_list[1:])
            # if the first value is between
            else:
                # remove the between value
                result = sum_max_min(my_list[0:2] + my_list[3:])
        # check if its smaller than the surrounding
        else:
            # if the second is larger
            if (my_list[2] > my_list[0]):
                # remove the in between value
                result = sum_max_min(my_list[1:])
            # if the first is larger
            else:
                # remove the in between value
                result = sum_max_min(my_list[0:2] + my_list[3:])
    # return the second lowest
    return result
