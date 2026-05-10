# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Start searching from the root of the tree
        cur = root

        # Traverse the tree until we find the split point
        while cur:
            # Check if BOTH p and q are strictly GREATER than the current node.
            # In a Binary Search Tree (BST), this means both nodes must be in the right subtree.
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right  # Move down to the right child
            
            # Check if BOTH p and q are strictly LESS than the current node.
            # This means both nodes must be in the left subtree.
            # NOTE: This must be an 'elif' so it only checks if the first condition was false.
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left   # Move down to the left child
            
            # We have found the split point. This happens if:
            # 1. p is on one side of cur, and q is on the other.
            # 2. cur is exactly equal to p (and q is below it).
            # 3. cur is exactly equal to q (and p is below it).
            # In all these cases, 'cur' is guaranteed to be the Lowest Common Ancestor.
            else:
                return cur