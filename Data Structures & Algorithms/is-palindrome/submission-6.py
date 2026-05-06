class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers:
        # l starts from the beginning of the string
        # r starts from the end of the string
        l, r = 0, len(s) - 1

        # Continue checking while left pointer is before right pointer
        while l < r:

            # Move left pointer forward until it points to an alphanumeric character
            # Skip spaces, punctuation, and special characters
            while l < r and not self.alphaNum(s[l]):
                l += 1

            # Move right pointer backward until it points to an alphanumeric character
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            # Compare characters in lowercase to ensure case-insensitive comparison
            # If mismatch found → not a palindrome
            if s[l].lower() != s[r].lower():
                return False

            # Move both pointers toward the center
            l += 1
            r -= 1

        # If all character pairs matched → string is a palindrome
        return True
    
    def alphaNum(self, c):
        # Returns True if character is alphanumeric:
        # 1. Uppercase letter (A–Z)
        # 2. Lowercase letter (a–z)
        # 3. Digit (0–9)
        return (
            ord('A') <= ord(c) <= ord('Z') or  # Check uppercase
            ord('a') <= ord(c) <= ord('z') or  # Check lowercase
            ord('0') <= ord(c) <= ord('9')     # Check digit
        )

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(1)
