class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers:
        # l -> left boundary of search space
        # r -> right boundary of search space
        l, r = 0, len(nums) - 1

        # Continue searching while the search space is valid
        # (i.e., left pointer has not crossed right pointer)
        while l <= r:
            # Find the middle index of the current search space
            # Using floor division to avoid decimals
            m = (l + r) // 2

            # If middle element is greater than target,
            # the target must be in the left half (if it exists)
            if nums[m] > target:
                r = m - 1  # Move right pointer to one position left of middle

            # If middle element is smaller than target,
            # the target must be in the right half
            elif nums[m] < target:
                l = m + 1  # Move left pointer to one position right of middle

            # If middle element equals target, we found it
            else:
                return m  # Return the index of target

        # If we exit the loop, the target was not found
        return -1

# Time & Space Complexity
# Time complexity: O(log⁡n)
# Space complexity: O(1)
