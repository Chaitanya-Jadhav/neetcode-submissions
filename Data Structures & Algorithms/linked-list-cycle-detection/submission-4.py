# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If the list is empty or has only one node with no next, there can't be a cycle.
        # However, the loop condition below also handles this gracefully.
        slow, fast = head, head  # Initialize two pointers at the start: slow advances 1 step, fast advances 2 steps.

        # Move through the list until 'fast' reaches the end (None) or there is no next node to advance to.
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1 step
            fast = fast.next.next     # Move fast pointer by 2 steps

            # If the two pointers meet, a cycle exists.
            if slow == fast:
                return True

        # If we exit the loop, 'fast' reached the end and there is no cycle.
        return False