class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. INITIALIZE POINTERS
        # 'l' (left) points to the start of the array.
        # 'r' (right) points to the end of the array.
        # This defines our initial search space as the entire array.
        l, r = 0, len(nums) - 1

        # 2. LOOP CONDITION
        # Continue searching as long as the search space is valid.
        # We use '<=' because we still need to check the element if l and r point to the exact same index.
        while l <= r:
            
            # 3. FIND THE MIDDLE
            # Calculate the middle index 'm'. 
            # The '//' operator in Python performs integer division (flooring the result).
            m = (l + r) // 2

            # 4. COMPARE AND NARROW SEARCH SPACE
            # Case A: The middle element is TOO BIG.
            # Since the array is sorted, everything to the right of 'm' is also too big.
            # We can safely discard the right half by moving our right pointer 'r' to 'm - 1'.
            if nums[m] > target:
                r = m - 1
            
            # Case B: The middle element is TOO SMALL.
            # Similarly, everything to the left of 'm' is also too small.
            # We discard the left half by moving our left pointer 'l' to 'm + 1'.
            elif nums[m] < target:
                l = m + 1
            
            # Case C: TARGET FOUND.
            # The middle element is exactly our target. Return its index.
            else:
                return m
        
        # 5. TARGET NOT FOUND
        # If the while loop finishes and we haven't returned 'm', the target doesn't exist in the array.
        return -1