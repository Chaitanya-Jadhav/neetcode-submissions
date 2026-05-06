class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers:
        # l starts at the beginning of the array
        # r starts at the end of the array
        l, r = 0, len(numbers) - 1

        # Continue until the two pointers meet
        while l < r:
            # Calculate the current sum of the two numbers
            curSum = numbers[l] + numbers[r]

            # If current sum is greater than target,
            # we need a smaller sum → move right pointer left
            if curSum > target:
                r -= 1

            # If current sum is smaller than target,
            # we need a larger sum → move left pointer right
            elif curSum < target:
                l += 1

            # If current sum equals target,
            # return 1-based indices as required by the problem
            else:
                return [l + 1, r + 1]

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(1)
