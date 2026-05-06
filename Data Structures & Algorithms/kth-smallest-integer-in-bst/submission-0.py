# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Finds the k-th smallest element in a Binary Search Tree (BST).
        Uses in-order traversal (which visits nodes in ascending order in a BST).
        """

        n = 0  # Counter to keep track of how many nodes have been visited
        stack = []  # Stack for iterative in-order traversal
        curr = root  # Start traversal from the root

        # Continue while there are nodes to process either in the stack or via curr
        while curr or stack:
            # Go as left as possible (left subtree first in in-order traversal)
            while curr:
                stack.append(curr)
                curr = curr.left

            # Pop the node from the stack (next node in in-order)
            curr = stack.pop()
            n += 1  # Increment the count of visited nodes

            # If we've reached the k-th node, return its value
            if n == k:
                return curr.val

            # Move to the right subtree to continue traversal
            curr = curr.right
