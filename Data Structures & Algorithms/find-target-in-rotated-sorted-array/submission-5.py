class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers for binary search
        # l = left pointer (start of array)
        # r = right pointer (end of array)
        l, r = 0, len(nums) - 1

        # Continue searching while the search space is valid
        while l <= r:
            # Find the middle index
            mid = (l + r) // 2

            # If the middle element is the target, return its index
            if target == nums[mid]:
                return mid
            
            # Check if the left half (l to mid) is sorted
            if nums[l] <= nums[mid]:

                # If target is NOT within the sorted left half,
                # discard the left half and search in the right half
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    # Otherwise, search in the left half
                    r = mid - 1

            # Otherwise, the right half (mid to r) must be sorted
            else:

                # If target is NOT within the sorted right half,
                # discard the right half and search in the left half
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    # Otherwise, search in the right half
                    l = mid + 1

        # If the target is not found, return -1
        return -1

# Time & Space Complexity
# Time complexity: O(log⁡n)
# Space complexity: O(1)

