class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: If either number is "0", the product is "0".
        if "0" in [num1, num2]:
            return "0"

        # The maximum possible length of the product is the sum of the lengths of both numbers.
        # We initialize an array with zeros to hold the results of each digit multiplication.
        res = [0] * (len(num1) + len(num2))
        
        # Reverse both strings. 
        # This makes it easier to start multiplying from the least significant digits (the ones place) 
        # at index 0, moving towards the most significant digits.
        num1, num2 = num1[::-1], num2[::-1]
        
        # Loop through each digit of the first number
        for i1 in range(len(num1)):
            # Loop through each digit of the second number
            for i2 in range(len(num2)):
                # Multiply the two digits together
                digit = int(num1[i1]) * int(num2[i2])
                
                # Add the result to the correct position in the array.
                # The position is determined by the sum of their indices (i1 + i2).
                res[i1 + i2] += digit
                
                # Handle the carry-over. 
                # If the value at the current position is 10 or greater, 
                # we add the tens place to the NEXT position (i1 + i2 + 1).
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                
                # Keep only the ones place digit at the current position.
                res[i1 + i2] = res[i1 + i2] % 10

        # Reverse the result array back to its correct order (most significant digit first).
        # Initialize a pointer 'beg' (beginning) to help remove any leading zeros.
        res, beg = res[::-1], 0
        
        # Increment 'beg' to skip over any leading zeros at the start of the array.
        # (e.g., turning [0, 0, 1, 2, 3] into a start index of 2)
        while beg < len(res) and res[beg] == 0:
            beg += 1
            
        # Slice the array from the first non-zero digit to the end,
        # and convert all the integers back into strings.
        res = map(str, res[beg:])
        
        # Join the array of strings into one single string and return it.
        return "".join(res)