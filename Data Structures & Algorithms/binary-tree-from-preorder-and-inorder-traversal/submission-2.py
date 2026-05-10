# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: If there are no elements left to process in our lists,
        # we have reached a leaf's child. Return None to represent an empty subtree.
        if not preorder or not inorder:
            return None
        
        # 1. Identify the Root
        # The first element in a preorder array is always the root of the current subtree.
        root = TreeNode(preorder[0])
        
        # 2. Find the Root in the Inorder Array
        # We find the index of the root value in the inorder list. 
        # Elements to the left of this index form the left subtree.
        # Elements to the right of this index form the right subtree.
        # Conveniently, 'mid' also equals the number of nodes in the left subtree.
        mid = inorder.index(preorder[0])

        # 3. Build the Left Subtree
        # preorder slice: Start at index 1 (skipping the current root) and take 'mid' elements (up to mid+1).
        # inorder slice: Take everything from the start up to the 'mid' index (excluding the root).
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # 4. Build the Right Subtree
        # preorder slice: Take everything after the left subtree's elements (from mid+1 to the end).
        # inorder slice: Take everything after the root's index (from mid+1 to the end).
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # 5. Return the constructed subtree
        # Once the left and right subtrees are built and attached, return the current root.
        return root