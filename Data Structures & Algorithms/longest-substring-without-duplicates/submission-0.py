class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # To store unique characters in the current window
        l = 0            # Left pointer of the sliding window
        res = 0          # Variable to store the maximum length found

        # Iterate through the string using the right pointer
        for r in range(len(s)):
            # If the character at right pointer is already in the set,
            # shrink the window from the left until it's removed
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # Add the current character to the set
            charSet.add(s[r])

            # Update the maximum length found so far
            res = max(res, r - l + 1)

        # Return the length of the longest substring without repeating characters
        return res
