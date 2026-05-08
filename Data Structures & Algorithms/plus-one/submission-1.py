class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Reverse the list so the ones place is at index 0. 
        # This makes it easier to iterate and append if the number grows.
        digits = digits[::-1]
        
        # 'one' acts as our carry value. We initialize it to 1 because we are adding one.
        # 'i' is our pointer tracking the current index.
        one, i = 1, 0

        # The loop runs as long as we still have a carry to add.
        while one:
            # Check if our pointer is still within the existing digits list.
            if i < len(digits):
                # If the current digit is 9, adding 1 results in 10.
                # We place a 0 here, and 'one' stays 1 to carry over to the next loop.
                if digits[i] == 9:
                    digits[i] = 0
                # If the digit is less than 9, there is no carry-over.
                else:
                    digits[i] += 1
                    one = 0  # Set carry to 0 to break the loop.
            
            # If our pointer exceeds the list length, it means we had a carry 
            # that requires a new digit (e.g., 99 + 1 = 100).
            else:
                digits.append(1) # Add the new highest place value.
                one = 0          # Set carry to 0 to break the loop.
            
            # Move to the next place value (tens, hundreds, etc.).
            i += 1
        
        # Reverse the list back to its original orientation before returning.
        return digits[::-1]