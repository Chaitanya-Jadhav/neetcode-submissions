# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function using Depth-First Search (DFS)
        # It returns a list containing two values for any given node: [is_balanced, height]
        def dfs(root):
            # Base case: We've reached an empty node (leaf's child).
            # An empty tree is perfectly balanced (True) and has a height of 0.
            if not root:
                return [True, 0]
            
            # Post-order traversal: Visit left and right children first (Bottom-up approach).
            # left and right will hold lists like [True/False, height] for their respective subtrees.
            left, right = dfs(root.left), dfs(root.right)
            
            # The current node's subtree is considered balanced ONLY IF all three conditions are met:
            # 1. The left subtree is balanced (left[0] is True)
            # 2. The right subtree is balanced (right[0] is True)
            # 3. The absolute difference in heights between left and right subtrees is <= 1
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            # Return the data for the current node up to its parent:
            # Index 0: The boolean result of whether this specific subtree is balanced.
            # Index 1: The height of this subtree (1 for the current node + max height of its children).
            return [balanced, 1 + max(left[1], right[1])]
        
        # Trigger the DFS starting at the root. 
        # dfs(root) returns [is_balanced, total_height]. 
        # We only care about the boolean result, so we return the value at index 0.
        return dfs(root)[0]