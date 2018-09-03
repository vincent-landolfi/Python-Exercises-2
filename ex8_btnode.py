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
    
    def set_depth(self,depth):
        ''' (BTNode,int) -> NoneType
        Sets the depth of the node to the given depth
        and all the nodes lower than it as well
        '''
        # set the depth of the current node
        self.depth = depth
        # check if the right is none
        if self.right is not None:
            # recurse through the tree on the right
            self.right.set_depth(depth+1)
        # check if the left is none
        if self.left is not None:
            # recurse the tree on the left
            self.left.set_depth(depth+1)
            
    def leaves_and_internals(self,leaves = set(),internals = set()):
        '''(BTNode) -> tuple of sets
        Starts at a node and returns a tuple of two
        sets, the first being all the leaves of the tree,
        and the second being all the internal nodes
        '''
        # check if its a leaf node
        if self.right is None and self.left is None:
            # add it to the first tuple
            leaves.add(self.value)
        # check if it only has one child
        # check if it has children
        else:
            # add it to the second set
            internals.add(self.value)
            # check if there is something to the left
            if self.left is not None:
                # go through left node
                self.left.leaves_and_internals()
            # check if there is something to the right
            if self.right is not None:
                # go through right now
                self.right.leaves_and_internals()
        # return the tuple
        return (leaves,internals)
    
    def pre_order(self,L=[]):
        L.append(self.value)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
        return L
    
    def in_order(self,L=[]):
        if self.left is None:
            L.append(self.value)
            if self.right is not None:
                self.right.in_order()
        else:
            if self.left:
                self.left.in_order()
            L.append(self.value)
            if self.right:
                self.right.in_order()
        return L
    
    def post_order(self):
        L = []
        if self.left is None and self.right is None:
            L.append(self.value)
        else:
            if self.left:
                L.extend(self.left.post_order())
            if self.right:
                L.extend(self.right.post_order())
            L.append(self.value)
        return L
    
    def helper(self,L = [0,0]):
        L[1]+=1
        L[0]+=self.value
        if self.left:
            self.left.helper()
        if self.right:
            self.right.helper()
        return (L)
    
    def average(self):
        my_list = self.helper()
        return (my_list[0]/my_list[1])
    
    def reverse(self):
        if self.right is None and self.left is None:
            holder = self.left
            self.left = self.right
            self.right = holder
        else:
            if self.left:
                self.left.reverse()
            if self.right:
                self.right.reverse()
    
    def decrypt(self,code):
        if code == '':
            result = self.value
        else:
            if code[0] == '_':
                result = self.left.decrypt(code[1:])
            else:
                result = self.right.decrypt(code[1:])
        return result
    
    def hk(self,word):
        L = word.split()
        new = ''
        for i in L:
            new += self.decrypt(i)
        return new
    
if(__name__ == "__main__"):
    # just a simple tree to practice on
    my_tree = BTNode(10, BTNode(3, BTNode(5), BTNode(2)),
                     BTNode(7, BTNode(4, BTNode(9)), BTNode(6)))
    print(my_tree)
    
    morse = BTNode('start', BTNode('T',BTNode('M',BTNode('O',BTNode('-',BTNode('0'),BTNode('9')),BTNode('.',None,BTNode('8'))),BTNode('G',BTNode('Q'),BTNode('Z',None,BTNode('7')))),
                                   BTNode('N',BTNode('K',BTNode('Y'),BTNode('C')),BTNode('D',BTNode('X'),BTNode('B',None,BTNode('6'))))),
                                   BTNode('E',BTNode('A',BTNode('W',BTNode('J',BTNode('1'),None),BTNode('P')),BTNode('R',None,BTNode('L'))),
                                          BTNode('I',BTNode('U',BTNode('-',BTNode('2'),None),BTNode('F')),BTNode('S',BTNode('V',BTNode('3'),None),
                                                                                                                 BTNode('H',BTNode('4'),BTNode('5'))))))