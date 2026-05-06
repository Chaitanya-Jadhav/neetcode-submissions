class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize the result variable to 0.
        # We start with 0 because 0 XORed with any number 'n' is just 'n'.
        res = 0

        # Loop through every number in the given list.
        for n in nums:
            # Continuously XOR the current result with the current number 'n'.
            # As the loop runs, duplicate numbers will XOR with each other and become 0.
            # For example, if nums = [2, 1, 2], the operations are:
            # 0 ^ 2 = 2
            # 2 ^ 1 = 3
            # 3 ^ 2 = 1 (The 2s cancel out, leaving the 1)
            res = res ^ n
        
        # After the loop finishes, all pairs have canceled out.
        # 'res' now holds the only number that didn't have a pair.
        return res