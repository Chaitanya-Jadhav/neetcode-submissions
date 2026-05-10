# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize our global maximum result. 
        # We start with root.val instead of 0 because tree nodes can contain negative values.
        res = root.val
        
        # Helper function to perform Depth-First Search (DFS).
        # What it computes: The maximum path sum starting from 'root' and going straight down ONE branch.
        def dfs(root):
            nonlocal res # This allows us to modify the 'res' variable defined in the outer scope

            # Base case: an empty node contributes 0 to any path sum.
            if not root:
                return 0
            
            # 1. Recursively get the max path sums from the left and right children.
            leftMax = dfs(root.left)
            rightMax= dfs(root.right)

            # 2. Filter out negative paths.
            # If a subtree returns a negative sum, adding it would only decrease our total.
            # By taking max(..., 0), we essentially say "if the branch is negative, don't include it at all."
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # 3. Calculate the sum IF the path "splits" at the current node.
            # A split means the path goes up the left subtree, crosses the current node, 
            # and goes down the right subtree. 
            # We update our global 'res' if this inverted "V" shaped path is the largest we've seen.
            res = max(res, root.val + leftMax + rightMax)

            # 4. Return the sum to the parent node.
            # A valid path can only branch once. The parent calling this function can only 
            # travel down ONE side of this current node. Therefore, we return the value 
            # of the current node plus the best single straight path (either left or right).
            return root.val + max(leftMax, rightMax)

        # Kick off the recursive traversal starting at the root
        dfs(root)

        # Return the highest path sum found during the traversal
        return res