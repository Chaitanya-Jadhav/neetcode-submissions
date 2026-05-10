# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # Helper function to perform Depth-First Search (DFS)
        # 'node' is the current node we are visiting.
        # 'maxValue' is the highest value we've seen on the path from the root to this node.
        def dfs(node, maxValue):
            
            # Base case: if we reach a null node (end of a branch), return 0 good nodes.
            if not node:
                return 0
            
            # Determine if the current node is "good".
            # It's good if its value is greater than or equal to the max value seen so far.
            res = 1 if node.val >= maxValue else 0
            
            # Update the maximum value seen so far for the next recursive calls.
            # If the current node's value is higher, it becomes the new maxValue for its children.
            maxValue = max(maxValue, node.val)
            
            # Recursively traverse the left subtree and add the good nodes found there to our result.
            res += dfs(node.left, maxValue)
            
            # Recursively traverse the right subtree and add the good nodes found there to our result.
            res += dfs(node.right, maxValue)
            
            # Return the total number of good nodes found in the subtree rooted at the current node.
            return res
        
        # Kick off the DFS starting at the root.
        # The initial max value is the root's own value, meaning the root is always considered a "good" node.
        return dfs(root, root.val)