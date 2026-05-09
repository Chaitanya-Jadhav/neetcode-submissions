# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers. 
        # 'prev' will track the node behind our current position (starts as None because the new tail points to None).
        # 'curr' is the current node we are processing, starting at the original head.
        prev, curr = None, head

        # Traverse the list until 'curr' falls off the end (becomes None).
        while curr:
            # STEP 1: Save the next node. 
            # We are about to break the link to the rest of the list, so we MUST save the next node to a temporary variable.
            temp = curr.next
            
            # STEP 2: Reverse the link. 
            # Take the current node's 'next' pointer and turn it around to point at the previous node.
            curr.next = prev
            
            # STEP 3: Shift 'prev' forward. 
            # The current node is now fully processed, so it becomes the 'prev' node for the next iteration.
            prev = curr
            
            # STEP 4: Shift 'curr' forward. 
            # Move on to the next node in the original list, which we safely tucked away in 'temp'.
            curr = temp
            
        # By the time the loop finishes, 'curr' has reached None, and 'prev' is resting on the very last node 
        # of the original list. This makes 'prev' the new head of the reversed list!
        return prev