# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # Hash map to map original nodes to their respective copied nodes.
        # Initializing with {None: None} cleanly handles edge cases where 
        # a node's 'next' or 'random' pointer points to a null value.
        oldToCopy = {None: None}

        cur = head
        
        # --- PASS 1: Create the clones ---
        # Traverse the original list to create a copy of each node (just the value).
        # We don't link them yet, we just store the 1:1 mapping in the dictionary.
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy  # Map the original node object to the new copy object
            cur = cur.next

        cur = head
        
        # --- PASS 2: Connect the clones ---
        # Traverse the original list again to assign 'next' and 'random' 
        # pointers to our newly created nodes.
        while cur:
            # Grab the copied node corresponding to the current original node
            copy = oldToCopy[cur]
            
            # Set the 'next' pointer by looking up the copy of the original's next node
            copy.next = oldToCopy[cur.next]
            
            # Set the 'random' pointer by looking up the copy of the original's random node
            copy.random = oldToCopy[cur.random]
            
            # Move to the next node in the original list
            cur = cur.next

        # Return the head of our deep-copied list, which is the copy of the original head
        return oldToCopy[head]