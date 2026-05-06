import math

class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer limits
        MIN = -2147483648  # -2^31
        MAX = 2147483647   #  2^31 - 1

        res = 0  # This will store the reversed number

        while x:
            # Get the last digit of x (handles negative numbers correctly using math.fmod)
            digit = int(math.fmod(x, 10))

            # Remove the last digit from x
            x = int(x / 10)

            # Check for overflow/underflow before multiplying and adding the digit
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0  # Overflow for positive numbers
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0  # Underflow for negative numbers

            # Append the digit to the result
            res = (res * 10) + digit

        return res
