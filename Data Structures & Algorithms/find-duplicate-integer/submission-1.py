class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize two pointers, slow (tortoise) and fast (hare).
        # We start both at index 0, which is outside any potential cycle.
        slow, fast = 0, 0
        
        # PHASE 1: Detect if a cycle exists and find the intersection point.
        while True:
            # Slow moves one step at a time (like nums[i])
            slow = nums[slow]
            
            # Fast moves two steps at a time (like nums[nums[i]])
            fast = nums[nums[fast]]
            
            # If slow and fast point to the same index, they have met inside the cycle.
            # This confirms a cycle exists (which means there is a duplicate).
            if slow == fast:
                break

        # PHASE 2: Find the entrance to the cycle (the actual duplicate number).
        # We leave 'slow' at the intersection point inside the cycle.
        # We create a new pointer 'slow2' and put it back at the start of the array.
        slow2 = 0
        
        while True:
            # Move both pointers one step at a time at the exact same speed.
            slow = nums[slow]
            slow2 = nums[slow2]
            
            # The mathematical property of Floyd's algorithm guarantees that 
            # the distance from the start to the cycle entrance is exactly equal 
            # to the distance from the intersection point to the cycle entrance.
            # Therefore, the exact point where they meet again is the start of the cycle.
            if slow == slow2:
                # The index where the cycle begins is the duplicate number.
                return slow