class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1s
        res = [1] * len(nums)

        prefix = 1  # Product of all elements to the left of the current index

        # First pass: build prefix products for each index
        for i in range(len(nums)):
            res[i] = prefix  # Set current res[i] to product of elements before it
            prefix *= nums[i]  # Update prefix with current number

        postfix = 1  # Product of all elements to the right of the current index

        # Second pass (right to left): multiply by postfix product for each index
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix  # Multiply with the product of elements after it
            postfix *= nums[i]  # Update postfix with current number

        # Return the final result array
        return res