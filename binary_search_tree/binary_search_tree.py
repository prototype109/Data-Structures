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
        current_node = None
        prev_node = None
        greater_than_prev_node = True

        if value >= self.value:
            if self.right is None:
                self.right = new_branch
                return
            else:
                current_node = self.right
        else:
            if self.left is None:
                self.left = new_branch
                return
            else:
                current_node = self.left

        while current_node:
            if value >= current_node.value:
                prev_node = current_node
                current_node = current_node.right
                greater_than_prev_node = True
            else:
                prev_node = current_node
                current_node = current_node.left
                greater_than_prev_node = False

        if greater_than_prev_node:
            prev_node.right = new_branch
        else:
            prev_node.left = new_branch
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
        contains_value = False
        current_node = None

        if target == self.value:
            contains_value = True
            return contains_value
        else:
            if target > self.value:
                current_node = self.right
            else:
                current_node = self.left

            while current_node:
                if current_node.value == target:
                    contains_value = True
                    return contains_value

                if current_node.value > target:
                    current_node = current_node.right
                else:
                    current_node = current_node.left


    # Return the maximum value found in the tree
    def get_max(self):
        current_max = self.value
        current_node = None

        if self.right is None:
            return current_max
        else:
            current_node = self.right
            while current_node:
                current_max = current_node.value
                current_node = current_node.right
            return current_max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
