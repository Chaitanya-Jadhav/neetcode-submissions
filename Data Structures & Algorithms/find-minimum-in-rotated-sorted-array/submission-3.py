class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize result with the first element
        # This guarantees we always return at least one valid value
        res = nums[0]
        
        # Initialize left and right pointers for binary search
        l, r = 0, len(nums) - 1

        # Perform binary search
        while l <= r:
            
            # If the current portion is already sorted,
            # then the leftmost element is the minimum
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break  # No need to continue searching
            
            # Calculate the middle index
            m = (l + r) // 2
            
            # Update result with the middle element
            # since it could potentially be the minimum
            res = min(res, nums[m])

            # If middle element is greater than or equal to left,
            # that means the left portion is sorted.
            # So the minimum must be in the right half.
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                # Otherwise, the pivot (minimum) is in the left half
                r = m - 1
        
        # Return the smallest value found
        return res
