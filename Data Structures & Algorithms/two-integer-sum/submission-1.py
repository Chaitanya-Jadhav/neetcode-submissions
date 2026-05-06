class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            print(difference)
            if difference in prevMap:
                return [prevMap[difference], i]
            else:
                prevMap[nums[i]] = i
        return False
