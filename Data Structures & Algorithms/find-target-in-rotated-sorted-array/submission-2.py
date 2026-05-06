# This class provides a method to search for a target value in a rotated sorted array.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for binary search
        l, r = 0, len(nums) - 1

        # Binary search loop continues while left pointer does not exceed right
        while l <= r:
            # Find the middle index
            m = (r + l) // 2

            # If the middle element is the target, return its index
            if nums[m] == target:
                return m
            
            # Determine if the left half is sorted
            if nums[l] <= nums[m]:
                # Check if the target lies outside the sorted left half
                if target > nums[m] or target < nums[l]:
                    # Target is not in the left half, move to the right half
                    l = m + 1
                else:
                    # Target is in the sorted left half
                    r = m - 1
            else:
                # Otherwise, the right half must be sorted
                # Check if the target lies outside the sorted right half
                if target < nums[m] or target > nums[r]:
                    # Target is not in the right half, move to the left half
                    r = m - 1
                else:
                    # Target is in the sorted right half
                    l = m + 1

        # If target is not found in the array, return -1
        return -1
