class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize a counter to keep track of the number of '1' bits
        res = 0

        # Loop continues as long as n is not strictly 0
        # (meaning there is at least one '1' bit left in the binary representation)
        while n:
            # The bitwise AND operation between n and (n-1) always flips 
            # the lowest (rightmost) set bit ('1') to a '0'.
            # Example: 
            #   n     = 12 (binary: 1100)
            #   n - 1 = 11 (binary: 1011)
            #   n & (n-1) = 1000 (The rightmost '1' in 1100 was removed)
            n = n & (n - 1)
            
            # Since we just cleared one '1' bit, we increment our counter
            res += 1
            
        # Return the total count of '1' bits found
        return res