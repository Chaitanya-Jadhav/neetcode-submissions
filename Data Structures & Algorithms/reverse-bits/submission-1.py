class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize result to 0. This will store the reversed bits.
        res = 0

        # Iterate through all 32 bits of the input number
        for i in range(32):
            # Extract the i-th bit from the right (0-indexed)
            bit = (n >> i) & 1

            # Place the extracted bit at the mirrored position (31 - i)
            res += (bit << (31 - i))

        # Return the final result after all bits are reversed
        return res
