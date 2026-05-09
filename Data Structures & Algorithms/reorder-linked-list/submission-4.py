# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
            
        # ==========================================
        # PHASE 1: Find the middle of the linked list
        # ==========================================
        # We use the fast and slow pointer technique (Tortoise and Hare).
        slow, fast = head, head.next

        # Advance 'fast' by two steps and 'slow' by one step.
        # When 'fast' reaches the end, 'slow' will be at the midpoint.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # ==========================================
        # PHASE 2: Reverse the second half of the list
        # ==========================================
        # 'slow.next' is the start of the second half.
        second = slow.next
        
        # Split the list into two separate halves by breaking the link.
        # 'prev' will eventually become the head of our reversed second half.
        prev = slow.next = None 
        
        # Standard linked list reversal logic
        while second:
            tmp = second.next      # Temporarily store the next node
            second.next = prev     # Reverse the pointer to face backward
            prev = second          # Move 'prev' forward to the current node
            second = tmp           # Move 'second' forward to the next node
        
        # ==========================================
        # PHASE 3: Merge the two halves alternately
        # ==========================================
        # 'first' points to the head of the first half.
        # 'second' (now 'prev' after reversal) points to the head of the reversed second half.
        first, second = head, prev
        
        # Interleave the nodes one by one
        while second:
            # Temporarily store the next nodes for both halves so we don't lose them
            tmp1, tmp2 = first.next, second.next
            
            # Link the current node of the first half to the current node of the second half
            first.next = second
            # Link the current node of the second half to the NEXT node of the first half
            second.next = tmp1
            
            # Move our 'first' and 'second' pointers forward for the next iteration
            first, second = tmp1, tmp2