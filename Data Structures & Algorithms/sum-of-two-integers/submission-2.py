class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Python integers have arbitrary precision (they can grow infinitely).
        # We use a 32-bit mask to simulate 32-bit integer boundaries, 
        # which forces the numbers to behave like they would in C++ or Java.
        mask = 0xFFFFFFFF 
        
        # This represents the maximum positive 32-bit integer (0111...111).
        # We will use this at the end to check if our result is negative.
        max_int = 0x7FFFFFFF

        # We keep looping until there is no carry left to add.
        while b != 0:
            # STEP 1: Calculate the carry.
            # The bitwise AND (a & b) finds the bits where both a and b are 1.
            # We shift it left by 1 (<< 1) because a carry moves to the next highest bit.
            carry = (a & b) << 1
            
            # STEP 2: Add without carry.
            # The bitwise XOR (a ^ b) adds the bits where only one of the bits is 1.
            # We apply the mask to ensure the result stays within 32 bits.
            a = (a ^ b) & mask
            
            # STEP 3: Assign the carry to b.
            # We will add this carry to 'a' in the next iteration of the loop.
            # Again, we apply the mask to keep it strictly 32-bit.
            b = carry & mask

        # Once the loop finishes (b == 0), 'a' holds our final 32-bit result.
        
        # If 'a' is less than or equal to max_int, it's a positive number, so we just return it.
        # If 'a' is greater than max_int, it means the 32nd bit (sign bit) is 1, making it a negative number.
        # To make Python understand it's a negative number (since Python doesn't naturally limit to 32 bits), 
        # we have to convert it back from 32-bit two's complement using ~(a ^ mask).
        return a if a <= max_int else ~(a ^ mask)