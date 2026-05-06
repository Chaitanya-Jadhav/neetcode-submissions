class Solution:
    def countBits(self, n: int) -> List[int]:
        # Create an array to store the number of 1-bits for each number from 0 to n.
        # It is initialized with 0s. 
        # Base case is inherently handled: dp[0] = 0 (since 0 has zero 1-bits).
        dp = [0] * (n + 1)
        
        # 'offset' tracks the highest power of 2 we have seen so far (1, 2, 4, 8...).
        # We start with 1, which is 2^0.
        offset = 1

        # Iterate through all numbers from 1 up to n to build our DP array.
        for i in range(1, n + 1):
            # Check if we have hit a new power of 2.
            # If the current offset multiplied by 2 equals 'i', 'i' is our new highest power of 2.
            if offset * 2 == i:
                offset = i
            
            # The core DP logic:
            # The number 'i' can be thought of as its most significant bit (the 'offset')
            # plus whatever is left over ('i - offset').
            # Therefore, the number of 1s in 'i' is 1 (for the offset bit) 
            # PLUS the number of 1s in the remainder, which we already calculated in dp[i - offset].
            # 
            # Example: i = 14 (1110 in binary). The highest power of 2 is offset = 8 (1000).
            # Remainder is 14 - 8 = 6 (0110). 
            # So, dp[14] = 1 + dp[6].
            dp[i] = 1 + dp[i - offset]
        
        # Return the fully populated array.
        return dp