# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the n-th node from the end of the list and returns the head of the modified list.
        Uses a two-pointer approach to do it in a single pass.
        """

        # Create a dummy node that points to the head.
        # This handles edge cases where the head node itself might be removed.
        dummy = ListNode(0, head)

        # Initialize two pointers: 'left' starts at dummy, 'right' starts at head.
        left = dummy
        right = head

        # Move 'right' n steps ahead so that the gap between 'left' and 'right' is n nodes.
        # This sets up the scenario where when 'right' reaches the end,
        # 'left' will be just before the node to remove.
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers one step at a time until 'right' reaches the end.
        # At this point, 'left' will be pointing to the node just before the target node.
        while right:
            left = left.next
            right = right.next

        # Remove the n-th node from the end by skipping the next node of 'left'.
        left.next = left.next.next

        # Return the new head of the list (could be different if the first node was removed).
        return dummy.next
