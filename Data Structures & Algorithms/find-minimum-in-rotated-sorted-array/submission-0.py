from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize result with the first element (acts as a fallback)
        res = nums[0]
        l, r = 0, len(nums) - 1  # Left and right pointers for binary search

        # Perform modified binary search
        while l <= r:
            # If subarray is already sorted, the leftmost element is the minimum
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break  # No need to continue, we found the minimum
            
            m = (l + r) // 2  # Find the middle index

            # Update the result with the minimum value found so far
            res = min(res, nums[m])

            # Determine which half to explore
            if nums[m] >= nums[l]:
                # Left half is sorted, so the pivot must be in the right half
                l = m + 1
            else:
                # Pivot is in the left half
                r = m - 1

        # Return the minimum value found
        return res
