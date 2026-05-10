# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # We use a helper function to pass down the valid boundaries (left, right)
        # 'left' is the absolute minimum value the node can be (exclusive)
        # 'right' is the absolute maximum value the node can be (exclusive)
        def valid(node, left, right):
            
            # Base Case: An empty tree (or reaching a leaf's child) is always a valid BST.
            if not node:
                return True
            
            # The BST rule: The current node's value must be strictly between 
            # our established left (min) and right (max) boundaries.
            # If it breaks this rule, we immediately return False.
            if not (node.val < right and node.val > left):
                return False
            
            # Recursive Step:
            # 1. Check the left subtree: 
            #    All nodes to the left must be LESS than the current node.
            #    So, we update the 'right' boundary to be the current node's value.
            # 2. Check the right subtree: 
            #    All nodes to the right must be GREATER than the current node.
            #    So, we update the 'left' boundary to be the current node's value.
            # Both subtrees must be valid, hence the 'and'.
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        # Initial call: The root node can theoretically be any value, 
        # so we start with boundaries of negative infinity and positive infinity.
        return valid(root, float("-inf"), float("inf"))