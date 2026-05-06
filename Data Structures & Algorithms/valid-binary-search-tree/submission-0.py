# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is a valid Binary Search Tree (BST).
        A BST must satisfy:
          - All nodes in the left subtree are less than the current node.
          - All nodes in the right subtree are greater than the current node.
          - Both left and right subtrees must also be BSTs.
        """

        def valid(node, left, right):
            # An empty node/subtree is valid by definition
            if not node:
                return True

            # The current node's value must lie strictly between 'left' and 'right' bounds
            if not (left < node.val < right):
                return False

            # Recursively validate the left and right subtrees:
            # - Left subtree must be less than current node's value
            # - Right subtree must be greater than current node's value
            return (
                valid(node.left, left, node.val) and
                valid(node.right, node.val, right)
            )

        # Start recursion with the full range of valid values for a BST
        return valid(root, float("-inf"), float("inf"))
