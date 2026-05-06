class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize result array with 1s.
        # res[i] will hold the product of all elements except nums[i].
        res = [1] * len(nums)

        # -------- LEFT (PREFIX) PASS --------
        # prefix will store the product of all elements to the LEFT of index i
        prefix = 1
        for i in range(len(nums)):
            # At index i, store the product of all elements before i
            res[i] = prefix

            # Update prefix by multiplying current element
            prefix *= nums[i]

        # -------- RIGHT (POSTFIX) PASS --------
        # postfix will store the product of all elements to the RIGHT of index i
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # Multiply current value (left product) by right product
            res[i] *= postfix

            # Update postfix by multiplying current element
            postfix *= nums[i]
        
        # Final result contains:
        # (product of elements to the left) * (product of elements to the right)
        return res

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity:
#     O(1) extra space.
#     O(n) space for the output array.
