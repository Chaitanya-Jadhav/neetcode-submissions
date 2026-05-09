class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # print(nums)
        for i, n in enumerate(nums):
            print(i,n)
            if n == nums[i]:
                continue