# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# This class provides a method to merge two sorted linked lists into a single sorted linked list.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases when building the new list
        # 'node' will be used to build the new merged list
        dummy = node = ListNode()
        
        # Traverse both lists while neither is empty
        while list1 and list2:
            # Compare the current nodes of both lists
            if list1.val < list2.val:
                # If list1's value is smaller, append it to the merged list
                node.next = list1
                # Move list1's pointer to the next node
                list1 = list1.next
            else:
                # Otherwise, append list2's node
                node.next = list2
                # Move list2's pointer to the next node
                list2 = list2.next
            # Advance the 'node' pointer to the last node in the merged list
            node = node.next
        
        # At this point, at least one of the lists is empty
        # Append the remaining non-empty list (if any) directly
        node.next = list1 or list2

        # Return the next node after dummy, which is the actual head of the merged list
        return dummy.next
