import sys
sys.path.append('../queue')
sys.path.append('../stack')
from queue import Queue
from stack import Stack

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_branch = BSTNode(value)
        
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = new_branch
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = new_branch
        # new_branch = BSTNode(value)
        # current_node = None
        # can_insert = False
        # current_left = self.left
        # current_right = self.right
        # current_value = self.value
        # prev_node = None

        # while not can_insert:
        #     if value >= current_value:
        #         if current_right is None:
        #             can_insert = True
        #             if prev_node is None:
        #                 self.right = new_branch
        #             else:
        #                 prev_node.right = new_branch
        #         else:
        #             prev_node = current_right
        #             current_left = prev_node.left
        #             current_value = prev_node.value
        #             current_right = current_right.right
        #     else:
        #         if current_left is None:
        #             can_insert = True
        #             if prev_node is None:
        #                 self.left = new_branch
        #             else:
        #                 prev_node.left = new_branch
        #         else:
        #             prev_node = current_left
        #             current_right = prev_node.right
        #             current_value = prev_node.value
        #             current_left = current_left.left

        


    # Return True if the tree contains the value
    # False if it does not
    
    def contains(self, target):
        if target == self.value:
            return True

        if target > self.value:
            if self.right:
                return self.right.contains(target)
        else:
            if self.left:
                return self.left.contains(target)
        
        return False
        


    # Return the maximum value found in the tree

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------
    

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        if node.left:
            node.in_order_print(node.left)
            
        print(node.value)

        if node.right:
            node.in_order_print(node.right)



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()

        queue.enqueue(node)

        while len(queue) > 0:
            current_node = queue.dequeue()
            print(current_node.value)

            if current_node.right:
                queue.enqueue(current_node.right)

            if current_node.left:
                queue.enqueue(current_node.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()

        stack.push(node)

        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)

            if current_node.right:
                stack.push(current_node.right)

            if current_node.left:
                stack.push(current_node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass 