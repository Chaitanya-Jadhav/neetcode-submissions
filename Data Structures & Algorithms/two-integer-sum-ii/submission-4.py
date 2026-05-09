class Solution: 
    def twoSum(self, numbers: List[int], target: int) -> List[int]: 
        # Initialize two pointers: 
        # 'l' (left) starts at the beginning of the array (index 0)
        # 'r' (right) starts at the end of the array (last index)
        l, r = 0, len(numbers) - 1 

        # Continue searching as long as the left pointer is strictly less than the right pointer.
        # This ensures we don't use the same element twice.
        while l < r: 
            # Calculate the sum of the elements at the current left and right pointers
            curSum = numbers[l] + numbers[r] 

            # If the current sum is greater than our target:
            # Because the array is sorted, we need a smaller number to reduce the sum.
            # Moving the right pointer to the left gives us a smaller number.
            if curSum > target: 
                r -= 1 

            # If the current sum is less than our target:
            # We need a larger number to increase the sum.
            # Moving the left pointer to the right gives us a larger number.
            elif curSum < target: 
                l += 1 

            # If the current sum equals the target:
            # We found our pair! The problem usually asks for 1-based indices (1-indexed), 
            # so we add 1 to both 'l' and 'r' before returning.
            else: 
                return [l + 1, r + 1]