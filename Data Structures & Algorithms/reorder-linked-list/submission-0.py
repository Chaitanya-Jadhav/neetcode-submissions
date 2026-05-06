# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders a singly linked list in the specific pattern:
        L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
        The function modifies the list in-place and uses O(1) extra space.
        """

        # Step 1: Find the middle of the linked list using slow and fast pointers.
        # 'slow' moves one step at a time, while 'fast' moves two steps.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list starting from slow.next
        # 'second' is the head of the second half of the list
        second = slow.next
        # Break the list into two halves by setting slow.next to None
        prev = slow.next = None

        # Reverse the second half of the list
        while second:
            temp = second.next      # Store next node
            second.next = prev      # Reverse the link
            prev = second           # Move 'prev' one step forward
            second = temp           # Move to the next node in the original list

        # After the loop, 'prev' is the new head of the reversed second half

        # Step 3: Merge the two halves, alternating nodes from each half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next  # Store next nodes

            first.next = second    # Link first list node to a node from the second list
            second.next = tmp1     # Link the second list node to the next node of the first list

            # Move the pointers forward for next merge step
            first, second = tmp1, tmp2
