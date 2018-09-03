class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.depth = 0  # the depth of this node in a tree

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, depth):
        ''' (BTNode,int) -> NoneType
        Sets the depth of the node to the given depth
        and all the nodes lower than it as well
        '''
        # set the depth of the current node
        self.depth = depth
        # check if the right is none
        if self.right is not None:
            # recurse through the tree on the right
            self.right.set_depth(depth + 1)
        # check if the left is none
        if self.left is not None:
            # recurse the tree on the left
            self.left.set_depth(depth + 1)

    def leaves_and_internals(self, leaves=set(), internals=set(), count=0):
        '''(BTNode) -> tuple of sets
        Starts at a node and returns a tuple of two
        sets, the first being all the leaves of the tree,
        and the second being all the internal nodes
        '''
        # check if its a leaf node
        if self.right is None and self.left is None:
            # add it to the first set
            leaves.add(self.value)
        # check if it only has one child
        # check if it has children
        else:
            if count != 0:
                # add it to the second set
                internals.add(self.value)
            # check if there is something to the left
            if self.left is not None:
                # go through left node
                self.left.leaves_and_internals(count=1)
            # check if there is something to the right
            if self.right is not None:
                # go through right now
                self.right.leaves_and_internals(count=1)
        # return the tuple
        return (leaves, internals)

    def sum_to_deepest(self):
        ''' (BTNode) -> int
        Returns the sum of all the values to
        the deepest node. If multiple nodes are equally deep,
        then it returns the largest of the multiple sums
        '''
        # preset values
        left = 0
        right = 0
        # check if the left node is there
        if (self.left):
            # recurse through that node
            left = self.left.sum_to_deepest()
        # check if the right node is there
        if (self.right):
            # recurse through that node
            right = self.right.sum_to_deepest()
        # return the max of the two plus the value
        return max(left, right) + self.value
    
    def height(self):
        left = 1
        right = 1
        if (self.left):
            left = 1 + self.left.height()
        if (self.right):
            right = 1 +self.right.height()
        return max(left,right)
    

if(__name__ == "__main__"):
    # just a simple tree to practice on
    my_tree = BTNode(10, BTNode(3, BTNode(5), BTNode(2)),
                     BTNode(7, BTNode(4, BTNode(9)), BTNode(6)))

    print(my_tree)
