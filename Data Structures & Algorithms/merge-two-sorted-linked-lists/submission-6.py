# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a sentinel/dummy node to act as the starting point
        # This avoids handling the head of the new list as a special case
        dummy = ListNode()
        tail = dummy

        # 2. Iterate while BOTH lists have remaining nodes
        while list1 and list2:
            # Compare values: pick the smaller one to maintain sorted order
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next # Move pointer in list1
            else:
                tail.next = list2
                list2 = list2.next # Move pointer in list2
            
            # Move the tail of our merged list forward
            tail = tail.next
        
        # 3. Handle remaining nodes
        # If one list is exhausted, just attach the remainder of the other
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # 4. Return the head of the merged list (skip the dummy node)
        return dummy.next