class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a 'dummy' node. This is a common linked list trick to simplify edge cases 
        # (like when the merged list is initially empty). We will build our new list attached to this dummy.
        dummy = ListNode()
        
        # 'tail' keeps track of the last node in our newly merged list.
        # It starts at the dummy node, and we will move it forward as we add new nodes.
        tail = dummy

        # Loop continues as long as BOTH lists still have nodes left to compare.
        while list1 and list2:
            
            # Compare the values at the current heads of list1 and list2.
            if list1.val < list2.val:
                # If list1 has the smaller value, point the tail's 'next' to list1's current node.
                tail.next = list1
                # Move the list1 pointer forward to its next node.
                list1 = list1.next
            else:
                # If list2 has the smaller (or equal) value, point the tail's 'next' to list2's current node.
                tail.next = list2
                # Move the list2 pointer forward to its next node.
                list2 = list2.next
            
            # Regardless of which node we picked, advance the 'tail' pointer
            # so it is ready to attach the next node in the next iteration.
            tail = tail.next
        
        # Once the while loop finishes, at least one of the lists is empty.
        # Since both lists are already sorted, we can just attach the entire remainder 
        # of the non-empty list directly to the end of our merged list.
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # Our merged list actually starts at the node AFTER the dummy node.
        return dummy.next