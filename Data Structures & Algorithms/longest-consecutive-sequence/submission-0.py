from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set for O(1) lookups
        numSet = set(nums)

        # Variable to store the length of the longest consecutive sequence found
        longest = 0

        # Iterate through each number in the original list
        for n in nums:
            # Only start counting when `n` is the beginning of a sequence
            # i.e., there is no number `n - 1` in the set
            if (n - 1) not in numSet:
                length = 0
                # Count how many consecutive numbers exist starting from `n`
                while (n + length) in numSet:
                    length += 1
                # Update longest if the current sequence is longer
                longest = max(length, longest)

        # Return the length of the longest consecutive sequence
        return longest
