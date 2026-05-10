# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BASE CASE: 
        # If we reach an empty node (either the tree is completely empty, 
        # or we stepped past a leaf node), the depth at this point is 0.
        # This condition prevents infinite loops and stops the recursion.
        if not root:
            return 0
        
        # RECURSIVE STEP:
        # If the node exists, we need to find out how deep its branches go.
        # 1. self.maxDepth(root.left) traverses down the entire left side.
        # 2. self.maxDepth(root.right) traverses down the entire right side.
        # 3. max(...) compares the two sides and picks the deeper one.
        # 4. We add 1 to account for the current node we are standing on.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))