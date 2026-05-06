# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Finds the lowest common ancestor (LCA) of two nodes in a Binary Search Tree (BST).
        The LCA is defined as the lowest node in the tree that has both p and q as descendants.
        Assumes all TreeNode values are unique and the tree is a valid BST.
        """

        curr = root  # Start traversal from the root node

        while curr:
            # If both p and q are less than current node, LCA must be in the left subtree
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left

            # If both p and q are greater than current node, LCA must be in the right subtree
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right

            else:
                # If the current node splits p and q (i.e., one is on the left, one on the right),
                # or if one of them is equal to curr, then curr is the LCA
                return curr
