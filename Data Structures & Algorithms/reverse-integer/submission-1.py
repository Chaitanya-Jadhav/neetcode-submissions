import math

class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer limits for overflow checking.
        MIN = -2147483648  # -2^31
        MAX = 2147483647   #  2^31 - 1

        res = 0
        
        # Keep looping until x becomes 0
        while x:
            # --- 1. EXTRACT THE LAST DIGIT ---
            # We use math.fmod() instead of the standard modulo operator (%).
            # Why? In Python, -1 % 10 results in 9. 
            # math.fmod(-1, 10) correctly gives -1.0, which we then cast to an int.
            digit = int(math.fmod(x, 10))
            
            # --- 2. SHRINK X ---
            # We divide by 10 and cast to int to truncate towards zero.
            # Why not use floor division (x // 10)? 
            # In Python, floor division rounds towards negative infinity. 
            # For example, -1 // 10 becomes -1, creating an infinite loop. 
            # int(-1 / 10) correctly becomes 0.
            x = int(x / 10)

            # --- 3. CHECK FOR POSITIVE OVERFLOW ---
            # We must check if multiplying 'res' by 10 and adding 'digit' will cross MAX.
            # - If res > 214748364 (MAX // 10), multiplying by 10 will definitely overflow.
            # - If res == 214748364, adding a digit strictly greater than 7 (MAX % 10) will overflow.
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
                
            # --- 4. CHECK FOR NEGATIVE OVERFLOW ---
            # Similar to the positive check, we ensure we don't cross MIN.
            # (Note: Python's floor division makes MIN // 10 evaluate to -214748365 and MIN % 10 to 2, 
            # but conceptually, this mirrors the positive overflow check for negative bounds).
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            
            # --- 5. BUILD THE RESULT ---
            # Shift the current result left by one decimal place (multiply by 10)
            # and add the newly extracted digit.
            res = (res * 10) + digit

        # Return the fully reversed integer
        return res