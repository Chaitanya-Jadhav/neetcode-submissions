class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: 'l' at the beginning and 'r' at the end of the string.
        l, r = 0, len(s) - 1

        # Continue checking as long as the left pointer is before the right pointer.
        while l < r:
            
            # Skip non-alphanumeric characters from the left.
            # We must also ensure 'l < r' inside this loop so the pointer doesn't go out of bounds.
            while l < r and not self.alphaNum(s[l]):
                l += 1
                
            # Skip non-alphanumeric characters from the right.
            # We check 'r > l' to ensure the right pointer doesn't cross the left one.
            while r > l and not self.alphaNum(s[r]):
                r -= 1
                
            # Compare the valid characters at both pointers. 
            # We convert both to lowercase to make the check case-insensitive.
            if s[l].lower() != s[r].lower():
                return False # If they don't match, it's not a palindrome.
            
            # If they matched, move both pointers inward to check the next pair.
            l += 1
            r -= 1
            
        # If the loop finishes without returning False, all valid characters mirrored each other perfectly.
        return True
    
    # Helper function to determine if a character is a letter or a number.
    def alphaNum(self, c):
        # ord() returns the ASCII value of the character. 
        # This checks if the character falls within the standard ASCII ranges for uppercase, lowercase, or digits.
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9') )