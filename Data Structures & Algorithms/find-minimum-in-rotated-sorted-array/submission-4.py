class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize the result with the first element just in case.
        res = nums[0]
        
        # Set up the left and right pointers for binary search.
        l, r = 0, len(nums) - 1

        while l <= r:
            # If the subarray from index 'l' to 'r' is already perfectly sorted,
            # the leftmost element (nums[l]) is strictly the minimum of this subarray.
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break # We can break out early since we found the absolute minimum of the remaining section.
            
            # Calculate the middle index.
            m = (l + r) // 2
            
            # Update our result with the middle element if it's smaller than the current result.
            res = min(res, nums[m])

            # Determine which half of the array to search next.
            # If the value at the middle index is greater than or equal to the left pointer's value,
            # it means the left half [l...m] is continuously sorted. 
            # Therefore, the "pivot" (and the minimum value) MUST be in the right half.
            if nums[m] >= nums[l]:
                l = m + 1
            
            # Otherwise, the right half is sorted, meaning the "pivot" (and minimum value)
            # must be located in the left half.
            else:
                r = m - 1
        
        # Return the lowest value found.
        return res