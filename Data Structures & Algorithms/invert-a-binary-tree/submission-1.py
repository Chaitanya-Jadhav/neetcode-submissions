# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree (i.e., swaps left and right children recursively or iteratively).
        This implementation uses an iterative approach with a stack.
        """

        # Base case: if the tree is empty, return None
        if not root:
            return None

        # Initialize a stack with the root node to perform iterative DFS
        stack = [root]

        # Process nodes until the stack is empty
        while stack:
            # Pop a node from the stack
            node = stack.pop()

            # Swap the left and right children of the current node
            node.right, node.left = node.left, node.right

            # If the left child exists (was originally the right), add it to the stack
            if node.left:
                stack.append(node.left)

            # If the right child exists (was originally the left), add it to the stack
            if node.right:
                stack.append(node.right)

        # Return the root of the now-inverted binary tree
        return root
