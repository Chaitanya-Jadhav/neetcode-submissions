# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs level-order traversal (BFS) of a binary tree.
        Returns a list of levels, where each level is a list of node values.
        """

        res = []  # Final result to store level-wise node values

        # Use a deque for efficient popping from the left (FIFO queue)
        q = collections.deque()
        q.append(root)  # Start with the root node

        while q:
            len_q = len(q)  # Number of nodes at the current level
            level = []      # List to hold values for this level

            for i in range(len_q):
                node = q.popleft()  # Get the next node in the queue
                if node:
                    level.append(node.val)     # Add node's value to current level
                    q.append(node.left)        # Add left child to the queue (if any)
                    q.append(node.right)       # Add right child to the queue (if any)

            if level:
                res.append(level)  # Only append non-empty levels to the result

        return res  # Return the list of levels

