class Solution:
    def myPow(self, x: float, n: int) -> float:
        # A nested helper function to handle the recursive logic for positive exponents
        def helper(x, n):
            # Base Case 1: If the base is 0, the result is always 0 (e.g., 0^5 = 0)
            if x == 0: return 0
            
            # Base Case 2: Any number to the power of 0 is 1 (e.g., 5^0 = 1)
            if n == 0: return 1

            # Recursive step: Divide the exponent by 2 (integer division)
            # This halves the work at each step, giving us O(log n) time complexity
            res = helper(x, n // 2)
            
            # Square the result of the halved exponent
            # E.g., if we want x^4, we find x^2 and multiply it by itself: (x^2) * (x^2)
            res = res * res

            # If the current exponent 'n' is odd, dividing by 2 left out one 'x'
            # E.g., x^5 // 2 = 2. So res is x^4. We must multiply by 'x' one more time.
            # If 'n' is even, simply return the squared result.
            return x * res if n % 2 else res
        
        # Call the helper function using the absolute value of n to guarantee a positive exponent
        res = helper(x, abs(n))
        
        # If the original n was positive or 0, return the result as-is.
        # If n was negative, mathematically x^-n is equal to 1 / (x^n).
        return res if n >= 0 else 1 / res