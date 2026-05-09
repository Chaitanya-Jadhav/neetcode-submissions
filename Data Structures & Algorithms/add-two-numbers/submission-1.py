# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node. This acts as a placeholder to simplify our code,
        # so we don't have to write special edge-case logic for the very first node.
        dummy = ListNode()
        
        # 'cur' (current) is the pointer we will use to build the new result list. 
        # It starts pointing at the dummy node.
        cur = dummy

        # Initialize the carry variable to 0. This holds the "tens" digit 
        # when the sum of a column is 10 or greater.
        carry = 0
        
        # We keep looping as long as there is a digit left in l1, OR a digit left in l2, 
        # OR a leftover carry that needs to be added as a new node.
        while l1 or l2 or carry:
            # Get the value from the current l1 node. 
            # If l1 has run out of nodes (is None), default to 0.
            v1 = l1.val if l1 else 0
            
            # Get the value from the current l2 node. 
            # If l2 has run out of nodes (is None), default to 0.
            v2 = l2.val if l2 else 0

            # Add the two digits together, plus any carry from the previous step.
            val = v1 + v2 + carry
            
            # Update the carry for the NEXT column.
            # Example: If val is 15, 15 // 10 = 1. The carry is 1.
            carry = val // 10
            
            # Update val to be ONLY the single digit for the CURRENT column.
            # Example: If val is 15, 15 % 10 = 5. We keep the 5.
            val = val % 10

            # Create a new node with this single digit and attach it to the end of our result list.
            cur.next = ListNode(val)

            # Move our building pointer ('cur') forward to the node we just created.
            cur = cur.next
            
            # Advance the l1 and l2 pointers to their next nodes to prepare for the next loop.
            # If a list has already reached the end, it stays None.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # The result list is attached after the dummy node. 
        # dummy.next points to the actual head of the resulting linked list.
        return dummy.next