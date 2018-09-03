from container import *
def banana_verify(source,goal,container,moves):
    ''' (str,str,Container,list of str) -> bool
    Takes the source word and uses the moves list as
    instructions as to what to do with the container.
    The goal of the function is to make sure that the
    ending word is the goal word.
    >>> banana_verify("BANANA","AAANNB",Stack,['P','M','P','M','P','M','G','G','G'])
    True
    >>> banana_verify("BANANA","AAABBN",Bucket,['P','P','G'])
    False
    '''
    # make a variable for the word we're building
    build = ''
    # make a variable telling if goal word is reached
    reached = False
    # go through the list of moves
    for i in moves:
        # go through all the possibilities
        # start with put
        if (i == 'P'):
            # check if its a bucket
            try:
                # pop out the first letter from source
                container.put(source[:1])
                # delete that letter from source
                source = source[1:]
            # if we get the error
            except ContainerFullException:
                # ruin the build word
                build = "ccccc"
        # if we want to move item
        elif (i == 'M'):
            # pop out the first letter of source
            # add it to build word
            build += source[:1]
            #delete letter
            source = source[1:]
        # if we want to get
        elif (i == 'G'):
            # try to get something from the container
            try:
                # and the gotten item to build
                build += container.get()
            # if its empty
            except ContainerEmptyException:
                # ruin the build word so its false
                build = "cccc"
    # check if the built word is the goal word
    if (build == goal):
        # goal has been reached
        reached = True
    # return if it was reached or not
    return reached