# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BASE CASE 1: Both nodes are empty (None).
        # This means we've successfully reached the end of a branch in both trees 
        # at the exact same time without finding any mismatches.
        if not p and not q:
            return True
        
        # BASE CASE 2: We found a mismatch. The trees are NOT identical if:
        # 1. 'not p' or 'not q': One node is empty but the other is not (a structural difference).
        # 2. 'p.val != q.val': Both nodes exist, but their values are different.
        if not p or not q or p.val != q.val:
            return False
        
        # RECURSIVE STEP: If we reach this line, it means both 'p' and 'q' exist 
        # AND their current values are equal. 
        # Now, we must verify that their left subtrees are identical AND their 
        # right subtrees are identical.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)