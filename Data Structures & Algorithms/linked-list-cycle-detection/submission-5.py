# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, 'slow' and 'fast', both starting at the head of the list.
        # This sets up our "Tortoise" (slow) and "Hare" (fast) for the race.
        slow, fast = head, head

        # The loop continues as long as 'fast' hasn't reached the end of the list.
        # We must check both 'fast' and 'fast.next' to ensure we can safely move the 
        # fast pointer two steps forward without throwing a NoneType attribute error.
        while fast and fast.next:
            
            # Move the 'slow' pointer forward by one node.
            slow = slow.next
            
            # Move the 'fast' pointer forward by two nodes.
            fast = fast.next.next
            
            # If a cycle exists, the 'fast' pointer will eventually loop around and 
            # "lap" the 'slow' pointer. When they point to the exact same node, 
            # we've confirmed a cycle exists.
            if slow == fast:
                return True
                
        # If the loop finishes naturally, it means the 'fast' pointer hit the end 
        # of the linked list (a None value). Therefore, there is no cycle.
        return False