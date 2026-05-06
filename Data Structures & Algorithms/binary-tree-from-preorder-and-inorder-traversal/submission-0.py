# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Reconstructs a binary tree from its preorder and inorder traversal arrays.
        
        preorder: Root -> Left -> Right
        inorder:  Left -> Root -> Right
        """

        # Base case: if either list is empty, there's no tree to build
        if not preorder or not inorder:
            return None

        # The first element in preorder is always the root of the current subtree
        root = TreeNode(preorder[0])

        # Find the index of the root value in inorder to divide left and right subtrees
        mid = inorder.index(preorder[0])

        # Recursively build the left subtree
        # preorder[1:mid+1] corresponds to the left subtree in preorder
        # inorder[:mid] corresponds to the left subtree in inorder
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        # Recursively build the right subtree
        # preorder[mid+1:] corresponds to the right subtree in preorder
        # inorder[mid+1:] corresponds to the right subtree in inorder
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # Return the constructed subtree root
        return root
