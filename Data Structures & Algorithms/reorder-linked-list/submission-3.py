# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorder the list in-place to follow the pattern:
        [0, n-1, 1, n-2, 2, n-3, ...]
        1) Find the middle of the list
        2) Reverse the second half
        3) Merge the two halves alternating nodes
        """
        # Edge case: empty or single-node list needs no work
        if head is None or head.next is None:
            return

        # 1) Find the middle of the list
        # Use slow/fast pointers. We want slow to point to the end of the first half.
        slow, fast = head, head.next
        # Move slow one step and fast two steps until fast reaches end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Split and reverse the second half
        # Second half starts after the middle node
        second = slow.next
        # Cut the list into two parts by setting the end of the first half to None
        # (Using a combined assignment for speed as in your original code)
        prev = slow.next = None

        # Reverse the second half in-place
        while second:
            tmp = second.next      # store next node
            second.next = prev     # reverse link
            prev = second          # advance prev
            second = tmp           # advance to next node

        # After reversal, 'prev' points to the head of the reversed second half
        first, second = head, prev

        # 3) Merge the two halves, taking one node from 'first', then one from 'second'
        while second:
            tmp1, tmp2 = first.next, second.next  # store next pointers
            first.next = second                    # link current first -> current second
            second.next = tmp1                       # link current second -> next of first half
            first, second = tmp1, tmp2                 # move both pointers forward

        # The list is modified in place; no return value is needed

