# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BASE CASE: 
        # If the current node is None (meaning we've hit the bottom of a branch 
        # or the tree is completely empty), stop and return None.
        if not root:
            return None

        # SWAP OPERATION:
        # Swap the left and right child nodes of the current root.
        # We use a temporary variable ('tmp') to hold the left child so we don't 
        # lose it when we overwrite root.left with root.right.
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # RECURSIVE CALLS:
        # Now that the current node's children are swapped, we need to invert 
        # their subtrees as well. 
        # Note: root.left and root.right have already been swapped above, 
        # but we still need to travel down both sides to invert the rest of the tree.
        self.invertTree(root.left)
        self.invertTree(root.right)

        # RETURN:
        # After the left and right subtrees have been fully inverted, 
        # return the current node.
        return root