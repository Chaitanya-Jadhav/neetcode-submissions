class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1s. 
        # We use 1 because it is the multiplicative identity (multiplying by 1 changes nothing).
        # This array will act as our output, making the space complexity O(1) extra space.
        res = [1] * len(nums)

        # --- FIRST PASS: Calculate Prefix Products ---
        # 'prefix' acts as a running total of the product of elements to the LEFT of index 'i'.
        prefix = 1
        for i in range(len(nums)):
            # 1. Store the product of everything to the left of 'i' in res[i].
            # For the very first element (i=0), there is nothing to the left, so it remains 1.
            res[i] = prefix
            
            # 2. Update the running 'prefix' by multiplying it with the current element.
            # This prepares the 'prefix' variable for the NEXT iteration.
            prefix *= nums[i]

        # --- SECOND PASS: Calculate Postfix Products ---
        # 'postfix' acts as a running total of the product of elements to the RIGHT of index 'i'.
        postfix = 1
        
        # Iterate backwards: from the last index down to 0.
        for i in range(len(nums) - 1, -1, -1):
            # 1. The current res[i] already holds the "left product" from the first pass.
            # We multiply it by the "right product" (postfix) to get the final answer for this index.
            res[i] *= postfix
            
            # 2. Update the running 'postfix' by multiplying it with the current element.
            # This prepares the 'postfix' variable for the NEXT iteration (moving leftwards).
            postfix *= nums[i]
        
        # The 'res' array now contains the product of all elements except self for every index.
        return res