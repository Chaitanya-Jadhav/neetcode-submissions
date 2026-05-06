from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort the input list to enable two-pointer technique

        # Step 2: Loop through each number in the sorted list
        for i, a in enumerate(nums):
            # Skip duplicate values for the first number to avoid repeated triplets
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Step 3: Set up two pointers — one from the left, one from the right
            l, r = i + 1, len(nums) - 1

            # Step 4: Use two-pointer approach to find pairs that sum with `a` to 0
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    # Sum too big, move right pointer left to decrease total
                    r -= 1
                elif threeSum < 0:
                    # Sum too small, move left pointer right to increase total
                    l += 1
                else:
                    # Valid triplet found
                    res.append([a, nums[l], nums[r]])

                    # Move left pointer to next distinct number to avoid duplicates
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        # Step 5: Return the list of unique triplets that sum to zero
        return res
