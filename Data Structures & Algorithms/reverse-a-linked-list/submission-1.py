# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# This class provides a method to reverse a singly linked list.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers:
        # 'prev' will eventually become the new head of the reversed list
        # 'curr' starts at the current node we are visiting (initially the head)
        prev, curr = None, head

        # Iterate through the list until we reach the end
        while curr:
            # Temporarily store the next node
            temp = curr.next
            # Reverse the link: point current node's next to the previous node
            curr.next = prev
            # Move 'prev' one step forward to current node
            prev = curr
            # Move 'curr' one step forward to the next node (saved in temp)
            curr = temp
        
        # At the end, 'prev' will be the new head of the reversed list
        return prev
