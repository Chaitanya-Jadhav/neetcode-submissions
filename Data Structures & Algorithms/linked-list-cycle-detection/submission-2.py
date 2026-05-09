# This class provides a method to detect if a linked list has a cycle.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers:
        # 'slow' moves one step at a time
        # 'fast' moves two steps at a time
        slow, fast = head, head

        # Loop through the list as long as 'fast' and 'fast.next' are valid
        while head and head.next:
            # Move slow pointer one step
            slow = slow.next
            # Move fast pointer two steps
            fast = fast.next.next
            # If the two pointers meet, there is a cycle
            if slow == fast:
                return True 
        
        # If we reach the end of the list, there is no cycle
        return False
