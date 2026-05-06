from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Expected sum of numbers from 0 to n
        sum_ = (n * (n + 1)) / 2

        # Actual sum of elements in the list
        sum_nums = sum(nums)

        # If both sums are equal, no number is missing
        if sum_ == sum_nums:
            return 0
        else:
            return int(sum_ - sum_nums)
