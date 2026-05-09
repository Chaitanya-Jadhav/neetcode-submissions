# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy node helps simplify edge cases, like when reversing the very first group.
        # It guarantees we always have a "previous" node to attach our reversed groups to.
        dummy = ListNode(0, head)
        
        # groupPrev points to the node immediately BEFORE the current k-group we are processing.
        # Initially, it's the dummy node.
        groupPrev = dummy

        while True:
            # Find the k-th node (the last node of our current group)
            kth = self.getKth(groupPrev, k)
            
            # If we don't have k nodes left, we are done. Break out of the loop
            # to leave the remaining nodes as they are.
            if not kth:
                break
            
            # Keep track of the node immediately AFTER the current k-group.
            # We need this to know when to stop reversing.
            groupNext = kth.next

            # --- REVERSE THE CURRENT K-GROUP ---
            
            # Initialize pointers for the standard linked list reversal.
            # 'prev' starts as kth.next (the node after the group) instead of None. 
            # This ensures the tail of our reversed group automatically connects to the rest of the list.
            prev, curr = kth.next, groupPrev.next
            
            # Reverse links until our 'curr' pointer passes the end of the group
            while curr != groupNext:
                tmp = curr.next  # Save the next node before overwriting the link
                curr.next = prev # Reverse the pointer to point backwards
                prev = curr      # Move 'prev' forward
                curr = tmp       # Move 'curr' forward

            # --- UPDATE POINTERS FOR THE NEXT ITERATION ---
            
            # Save the original first node of the group (which is now the last node after reversal).
            # This will become our 'groupPrev' for the next k-group.
            tmp = groupPrev.next
            
            # The 'kth' node is the new head of this reversed group. 
            # Connect the previous part of the list to this new head.
            groupPrev.next = kth
            
            # Move groupPrev to the end of the newly reversed group to prepare for the next iteration.
            groupPrev = tmp
            
        # Return the new head of the fully modified list (skipping the dummy node).
        return dummy.next

    def getKth(self, curr, k):
        # Helper function to traverse exactly k steps forward.
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr