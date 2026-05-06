class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # The expected range of numbers is from 0 to n. 
        # We find 'n' by getting the length of the provided list.
        n = len(nums)
        
        # Initialize our XOR accumulator with 'n'. 
        # We start with 'n' because the loop below only covers indices from 0 to n-1.
        xorr = n
        
        # Iterate through the array. 
        # 'i' represents the expected numbers (0 to n-1), and 'nums[i]' represents the actual numbers.
        for i in range(n):
            # The core logic: XOR the accumulator with the index 'i' AND the value 'nums[i]'.
            # Why this works: XORing a number with itself results in 0 (x ^ x = 0).
            # As we loop, every number that exists in the array will eventually be XORed 
            # against its corresponding index value. They will cancel each other out.
            xorr ^= i ^ nums[i]
            
        # The only value left in 'xorr' will be the index that never got cancelled out 
        # by a matching value in 'nums'. That is our missing number.
        return xorr