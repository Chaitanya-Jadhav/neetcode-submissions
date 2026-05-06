class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize a list to store the count of 1's in binary representation of each number from 0 to n
        dp = [0] * (n + 1)
        
        # Offset represents the most recent power of 2 (e.g., 1, 2, 4, 8, ...)
        offset = 1

        # Iterate through all numbers from 1 to n
        for i in range(1, n + 1):
            # If i reaches the next power of 2, update the offset
            if offset * 2 == i:
                offset = i
            # The number of 1's in binary of i is:
            # 1 (for the new most significant bit at offset) + count of 1's in (i - offset)
            dp[i] = 1 + dp[i - offset]

        return dp
