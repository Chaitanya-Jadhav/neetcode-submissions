# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # BASE CASE 1: If the subRoot is empty, it is technically a subtree of ANY tree.
        # This check must come first because an empty subRoot is always valid.
        if not subRoot:
            return True
        
        # BASE CASE 2: If the main root is empty (but subRoot is not, because it passed the above check),
        # we can't possibly find the subRoot here.
        if not root:
            return False
        
        # Check if the tree starting at the CURRENT 'root' node is identical to 'subRoot'.
        if self.sameTree(root, subRoot):
            return True
        
        # RECURSIVE STEP: If the current nodes didn't start a matching tree, 
        # recursively search down the left and right branches of the main tree.
        # If the subRoot is found in EITHER branch (hence the 'or'), we return True.
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    # Helper function to check if two trees are exactly identical
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If both nodes are completely empty, they match. We've hit the bottom of identical branches.
        if not root and not subRoot:
            return True
        
        # If BOTH nodes exist AND their values are exactly the same, 
        # we must continue checking to ensure their children also match.
        if root and subRoot and root.val == subRoot.val:
            # Recursively check the left children AND the right children. 
            # Both sides must match perfectly (hence the 'and').
            return (self.sameTree(root.left, subRoot.left) and
                self.sameTree(root.right, subRoot.right))
        
        # If we reach here, it means either:
        # 1. One node is empty and the other is not.
        # 2. Both nodes exist, but their values don't match.
        # In either case, the trees are not identical.
        return False