# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = [] # Array to store the sequence of node values

        # Helper function to perform Preorder DFS (Root, Left, Right)
        def dfs(node):
            # Base case: If the node is null, append a marker ("N") to represent it
            if not node:
                res.append("N")
                return
            
            # 1. Process the Root: Append the current node's value as a string
            res.append(str(node.val))
            
            # 2. Process the Left Child: Traverse down the left subtree
            dfs(node.left)
            
            # 3. Process the Right Child: Traverse down the right subtree
            dfs(node.right)
            
        # Start the traversal from the root
        dfs(root)
        
        # Join the array into a single comma-separated string (e.g., "1,2,N,N,3,4,N,N,5,N,N")
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Convert the comma-separated string back into a list of values
        vals = data.split(",")
        
        # Use a global/instance pointer to keep track of our current position in the 'vals' list
        self.i = 0

        # Helper function to reconstruct the tree using Preorder DFS
        def dfs():
            # Base case: If the current value is our null marker ("N")
            if vals[self.i] == "N":
                self.i += 1     # Move the pointer forward
                return None     # Return None to represent the null node
            
            # 1. Process the Root: Create a new TreeNode with the current integer value
            node = TreeNode(int(vals[self.i]))
            self.i += 1         # Move the pointer forward for the next recursive calls
            
            # 2. Process the Left Child: Recursively build the left subtree
            # Because of Preorder, the immediate next values belong to the left subtree
            node.left = dfs()
            
            # 3. Process the Right Child: Recursively build the right subtree
            node.right = dfs()

            # Return the fully constructed subtree rooted at this node
            return node
        
        # Start the recursive construction and return the resulting root node
        return dfs()