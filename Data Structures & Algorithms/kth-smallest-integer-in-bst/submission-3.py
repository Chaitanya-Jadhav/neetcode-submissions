# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # We use a stack to keep track of the nodes we need to visit, 
        # mimicking the call stack in a recursive approach.
        stack = []
        
        # Start our traversal at the root node.
        cur = root
        
        # Keep looping as long as we have a current node to process 
        # OR there are still nodes waiting in the stack.
        while cur or stack:
            
            # 1. Traverse as far left as possible.
            # In a BST, the left children are always smaller. Going all the 
            # way left ensures we find the absolute smallest elements first.
            while cur:
                stack.append(cur) # Save this node to process it later
                cur = cur.left    # Move down to the left child
            
            # 2. Process the node.
            # Pop the last node we saved. Because of the loop above, 
            # this will be the smallest unvisited node in the tree.
            cur = stack.pop()
            
            # 3. Count the node.
            # We just "visited" a node in sorted order, so we decrement k.
            k -= 1
            
            # 4. Check for our target.
            # If k has reached 0, we have found the kth smallest element!
            if k == 0:
                return cur.val
            
            # 5. Move to the right subtree.
            # According to in-order traversal rules, after visiting the left 
            # children and the node itself, we must visit the right children.
            cur = cur.right