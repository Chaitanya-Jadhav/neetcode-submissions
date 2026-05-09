# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. CREATE A DUMMY NODE
        # We use a dummy node placed right before the head. 
        # Why? It handles edge cases flawlessly—especially the case where the 
        # node we need to remove is the very first node (the head) of the list.
        dummy = ListNode(0, head)
        
        # 2. INITIALIZE TWO POINTERS
        # 'left' starts at the dummy node.
        # 'right' starts at the actual head of the list.
        left = dummy
        right = head

        # 3. CREATE THE "GAP"
        # Move the 'right' pointer forward by 'n' steps. 
        # This creates a fixed gap of exactly 'n' nodes between 'left' and 'right'.
        while n > 0 and right:
            right = right.next
            n -= 1

        # 4. SLIDE THE WINDOW TO THE END
        # Now move BOTH pointers forward at the same speed.
        # We stop when 'right' falls off the end of the list (becomes None).
        # Because we maintained that gap of 'n', the 'left' pointer will now be 
        # sitting exactly *one node before* the target node we want to remove.
        while right:
            left = left.next
            right = right.next

        # 5. DELETE THE NODE
        # 'left' is sitting right before the node we need to delete.
        # We bypass the target node by routing 'left's next pointer to the node AFTER the target.
        left.next = left.next.next

        # 6. RETURN THE NEW HEAD
        # We return dummy.next instead of 'head' because if the original head 
        # was the node we just removed, dummy.next will correctly point to the new head.
        return dummy.next