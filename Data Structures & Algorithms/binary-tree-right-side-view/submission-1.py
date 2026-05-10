# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # This will store the final list of right-side values
        res = []

        # Initialize a double-ended queue for BFS (Breadth-First Search)
        q = collections.deque()
        
        # Start by adding the root to the queue. 
        # (It's okay if root is None, the loop handles it)
        q.append(root)

        # Continue traversing as long as there are nodes in the queue
        while q:
            # rightSide will keep track of the rightmost node at the current level
            rightSide = None
            
            # Take a snapshot of the queue's length. 
            # This represents exactly how many nodes are on the CURRENT level.
            qLen = len(q)
            
            # Iterate through all nodes on this specific level
            for i in range(qLen):
                # Pop the node from the front of the queue
                node = q.popleft()
                
                # If the node is not null...
                if node:
                    # Update rightSide. Since we process left to right, 
                    # by the end of this loop, rightSide will hold the LAST (rightmost) node.
                    rightSide = node
                    
                    # Add the children to the queue for the NEXT level's processing.
                    # We add left first, then right, ensuring left-to-right order.
                    q.append(node.left)
                    q.append(node.right)
            
            # After processing the entire level, if we found at least one valid node,
            # append the value of the rightmost node we tracked to our result list.
            if rightSide: 
                res.append(rightSide.val)
                
        return res