# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Returns the maximum depth (height) of a binary tree.
        Depth is the number of nodes along the longest path from the root down to the farthest leaf node.
        This implementation uses recursion (depth-first traversal).
        """

        # Base case: if the current node is None, the depth is 0
        if not root:
            return 0

        # Recursively find the depth of the left subtree
        left_depth = self.maxDepth(root.left)

        # Recursively find the depth of the right subtree
        right_depth = self.maxDepth(root.right)

        # The maximum depth at the current node is the greater of the two subtrees' depths
        max_depth = max(left_depth, right_depth)

        # Add 1 to include the current node's level in the depth count
        return 1 + max_depth
