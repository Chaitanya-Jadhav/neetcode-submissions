# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # EDGE CASE: If the input array is empty or contains no lists, return None.
        if not lists or len(lists) == 0:
            return None

        # DIVIDE AND CONQUER: Keep merging lists in pairs until only 1 list remains.
        # This reduces the number of lists by half in each iteration.
        while len(lists) > 1:
            mergedLists = []
            
            # Iterate through the array of lists, taking them 2 at a time (step=2).
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # Ensure we don't go out of bounds if there is an odd number of lists.
                # If there's no pair for the last list, l2 becomes None.
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                # Merge the pair and append the resulting list to our temporary array.
                mergedLists.append(self.mergeList(l1, l2))
            
            # Overwrite the original lists array with our newly merged lists.
            # Next iteration will work on this smaller pool of lists.
            lists = mergedLists
            
        # Once the while loop ends, lists[0] holds the single, fully merged linked list.
        return lists[0]

    def mergeList(self, l1, l2):
        # DUMMY NODE: A common linked list trick to handle edge cases smoothly.
        # It gives us a guaranteed starting point so we don't have to write 
        # extra logic for the very first node insertion.
        dummy = ListNode()
        
        # 'tail' will act as our pointer that builds the new list, adding to the end.
        tail = dummy

        # TWO POINTERS: Compare the heads of both lists as long as neither is empty.
        while l1 and l2:
            if l1.val < l2.val:
                # l1's value is smaller, so link the tail to l1
                tail.next = l1
                # Move the l1 pointer forward
                l1 = l1.next
            else:
                # l2's value is smaller (or equal), so link the tail to l2
                tail.next = l2
                # Move the l2 pointer forward
                l2 = l2.next
            
            # Move the tail pointer forward so it's ready for the next insertion
            tail = tail.next

        # LEFTOVERS: If one list is longer than the other, one of these will trigger.
        # Because the leftover nodes are already sorted and linked, we can just 
        # attach the entire remaining segment to our tail at once.
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        # Return the actual start of the merged list, which skips our initial dummy node.
        return dummy.next