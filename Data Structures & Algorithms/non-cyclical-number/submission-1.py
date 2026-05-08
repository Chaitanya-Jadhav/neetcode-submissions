class Solution:
    def isHappy(self, n: int) -> bool:
        # We use a set to keep track of numbers we have already seen. 
        # This is crucial for cycle detection. If we see a number again 
        # before reaching 1, we are stuck in an infinite loop.
        visit = set()

        # Continue the loop as long as the current number 'n' 
        # hasn't been evaluated before.
        while n not in visit:
            # Add the current number to our 'seen' set
            visit.add(n)
            
            # Calculate the next number in the sequence 
            # using our helper function
            n = self.sumOfSquares(n)

            # If the sum of squares equals 1, the number is "happy"
            if n == 1:
                return True
                
        # If the while loop finishes, it means 'n' was found in 'visit'.
        # We hit a cycle without ever reaching 1, so the number is not happy.
        return False
    
    def sumOfSquares(self, n: int) -> int:
        output = 0
        
        # Process the number digit by digit until n becomes 0
        while n:
            # Get the rightmost digit (e.g., 19 % 10 = 9)
            digit = n % 10
            
            # Square the extracted digit
            digit = digit ** 2
            
            # Add the squared digit to our running total
            output += digit
            
            # Remove the rightmost digit from n by doing integer division 
            # (e.g., 19 // 10 = 1)
            n = n // 10
            
        return output