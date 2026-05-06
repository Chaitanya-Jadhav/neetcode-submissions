# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 'prev' starts as None because the new tail will point to nothing
        # 'curr' starts at the beginning of the original list
        prev, curr = None, head

        while curr:
            # 1. Save the next node before we break the link
            temp = curr.next 
            
            # 2. Reverse the link: point the current node backward to 'prev'
            curr.next = prev 
            
            # 3. Move the 'prev' window forward to the current node
            prev = curr 
            
            # 4. Move 'curr' forward to the saved 'temp' node to continue
            curr = temp 
            
        # When curr is None, prev is sitting on the new head of the reversed list
        return prev