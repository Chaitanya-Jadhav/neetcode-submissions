class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize the result variable to 0. 
        # This will act as a blank canvas to hold our reversed bits.
        res = 0
        
        # Loop 32 times because we are working with a standard 32-bit integer.
        for i in range(32):
            
            # 1. ISOLATE the current bit from the original number 'n'.
            # 'n >> i' shifts the bits to the right by 'i' positions, moving the target bit to the end.
            # '& 1' performs a bitwise AND, masking all other bits so we are left with exactly a 1 or a 0.
            bit = (n >> i) & 1
            
            # 2. PLACE the isolated bit in its new, reversed position.
            # 'bit << (31 - i)' shifts the bit to the left. 
            # (e.g., the 0th bit from the right becomes the 31st bit from the right).
            # 'res |' performs a bitwise OR, stamping this shifted bit into our result variable.
            res = res | (bit << (31 - i))
            
        # Return the final integer composed of the reversed bits.
        return res