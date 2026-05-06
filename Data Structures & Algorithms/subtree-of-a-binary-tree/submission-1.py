# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Checks whether 'subRoot' is a subtree of 'root'.
        A subtree is defined as a tree consisting of a node in 'root' and all of its descendants.
        """

        # If subRoot is None, it's always a subtree of any tree (including an empty one)
        if not subRoot:
            return True

        # If root is None but subRoot is not, then subRoot can't be a subtree
        if not root:
            return False
        
        # Check if the trees rooted at current nodes are the same
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise, recursively check left and right subtrees of 'root'
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Helper function to check if two binary trees are exactly the same.
        This is used to compare subtrees rooted at a given node.
        """

        # Both nodes are None, so trees are identical at this branch
        if not root and not subRoot:
            return True
        
        # If both nodes exist and values match, check subtrees recursively
        if root and subRoot and root.val == subRoot.val:
            return (
                self.isSameTree(root.left, subRoot.left) and  # Check left subtree
                self.isSameTree(root.right, subRoot.right)    # Check right subtree
            )
        else:
            # Nodes don't match or one is None — trees are not the same
            return False

        