# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # This will store our final result: a list of lists, where each inner list represents one level.
        res = []

        # Use a double-ended queue (deque) for O(1) removals from the front. 
        # A standard Python list would take O(N) time to pop from index 0.
        q = collections.deque()
        
        # Initialize the queue with the root node to start the traversal.
        q.append(root)
        
        # Continue traversing as long as there are nodes left to process in the queue.
        while q:
            # Capturing the length of the queue HERE is crucial. 
            # This length represents exactly how many nodes are on the CURRENT level.
            qLen = len(q)
            
            # This list will store the values of the nodes on the current level.
            level = []
            
            # Loop exactly 'qLen' times to process only the nodes on the current level.
            for i in range(qLen):
                # Remove the next node from the front of the queue.
                node = q.popleft()
                
                # Check if the node is actually a valid TreeNode (not None).
                if node:
                    # Add the node's value to our current level list.
                    level.append(node.val)
                    
                    # Add the left and right children to the back of the queue.
                    # Because we bound our 'for' loop to the original 'qLen', 
                    # these newly added children won't be processed until the NEXT iteration of the 'while' loop.
                    q.append(node.left)
                    q.append(node.right)
            
            # If our 'level' list is not empty (which can happen if the queue only contained None values),
            # append this level's values to our final result.
            if level:
                res.append(level)
                
        # Return the fully populated list of levels.
        return res