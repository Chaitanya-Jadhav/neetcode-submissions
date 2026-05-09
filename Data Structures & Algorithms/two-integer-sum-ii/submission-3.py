class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers: 
        # 'l' (left) points to the start of the array (smallest numbers).
        # 'r' (right) points to the end of the array (largest numbers).
        l, r = 0, len(numbers) - 1

        # Continue searching as long as the left pointer is before the right pointer.
        while l < r:
            # Calculate the sum of the two numbers currently pointed to.
            curSum = numbers[l] + numbers[r]

            # If the current sum is greater than our target:
            # We need a smaller sum. Since the array is sorted, we can only get 
            # a smaller sum by moving our right pointer to the left (to a smaller number).
            if curSum > target:
                r -= 1
                
            # If the current sum is less than our target:
            # We need a larger sum. We can only get a larger sum by moving 
            # our left pointer to the right (to a larger number).
            elif curSum < target:
                l += 1
                
            # If the current sum is exactly equal to our target:
            # We found the correct pair! 
            else:
                # The problem usually specifies a 1-indexed array for the return format,
                # meaning the first element is at index 1 instead of 0.
                # Therefore, we add 1 to both 'l' and 'r' before returning.
                return [l + 1, r + 1]