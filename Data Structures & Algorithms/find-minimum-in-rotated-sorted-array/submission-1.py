# This class provides a method to find the minimum element in a rotated sorted array.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize result with the first element of the array
        res = nums[0]
        
        # Initialize two pointers for binary search
        l, r = 0, len(nums) - 1

        # Binary search loop continues while the left pointer does not exceed the right
        while l <= r:
            # If the current subarray is already sorted,
            # then the smallest value must be at the left pointer
            if nums[l] < nums[r]:
                # Update the result with the smallest of the current result or nums[l]
                res = min(res, nums[l])
                # Since the subarray is sorted, we can break early
                break

            # Find the middle index
            m = (r + l) // 2
            # Update the result with the smallest of the current result or nums[m]
            res = min(res, nums[m])

            # Determine which half to search next
            if nums[m] >= nums[l]:
                # If the middle element is greater than or equal to the leftmost element,
                # it means the left part is sorted, so we search the right half
                l = m + 1
            else:
                # If not, it means the pivot (and hence the minimum) is in the left half
                r = m - 1

        # Return the minimum element found
        return res
