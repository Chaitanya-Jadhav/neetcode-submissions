class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_ = (n * (n + 1) ) / 2

        sum_nums = sum(nums)
        print(sum_,sum_nums)

        if sum_ == sum_nums:
            return 0
        else:
            return int(sum_ - sum_nums)
