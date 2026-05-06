# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Determines if two binary trees are structurally identical and the nodes have the same values.
        This is done using a recursive approach that compares nodes one-by-one.
        """

        # Base case 1: both nodes are None — trees are the same at this branch
        if not p and not q:
            return True

        # Base case 2: both nodes are not None and have the same value
        # Recursively check left and right subtrees
        if p and q and p.val == q.val:
            return (
                self.isSameTree(p.left, q.left) and  # Check left subtree
                self.isSameTree(p.right, q.right)    # Check right subtree
            )

        # Base case 3: one of the nodes is None, or the values do not match
        # Trees are not the same
        else:
            return False
