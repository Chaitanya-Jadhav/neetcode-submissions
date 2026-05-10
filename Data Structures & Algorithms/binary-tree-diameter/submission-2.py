# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # This variable keeps track of the maximum diameter found so far.
        # We use 'self.res' so its state is maintained across all recursive calls.
        self.res = 0

        # Helper function that performs Depth-First Search (DFS).
        # It calculates the maximum *height* of a given node's subtree,
        # while simultaneously checking if the *diameter* through that node is a new max.
        def dfs(curr):
            # Base case: if we reach an empty node (beyond a leaf), its height is 0.
            if not curr:
                return 0
            
            # Recursively calculate the maximum height of the left and right subtrees.
            left = dfs(curr.left)
            right = dfs(curr.right)

            # --- DIAMETER CALCULATION ---
            # The diameter passing THROUGH the current node is the sum of its left and right heights.
            # We update our global maximum if the current node's diameter is larger than the previous max.
            self.res = max(self.res, left + right)
            
            # --- HEIGHT CALCULATION (What gets returned to the parent) ---
            # To help the parent node calculate ITS diameter, we must return the height of the current node.
            # The height is 1 (accounting for the edge to the current node) plus the height of its tallest subtree.
            return 1 + max(left, right)
        
        # Kick off the DFS traversal starting from the root of the tree.
        dfs(root)
        
        # After traversing the whole tree, return the absolute maximum diameter found.
        return self.res