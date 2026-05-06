class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Dictionary to store frequency of characters in the current window
        res = 0     # Variable to store the length of the longest valid substring
        l = 0       # Left pointer for the sliding window

        # Iterate over the string with the right pointer
        for r in range(len(s)):
            # Increment the count of the current character
            count[s[r]] = 1 + count.get(s[r], 0)

            # If the number of characters to be replaced exceeds k, shrink the window
            # (r - l + 1) is the size of the current window
            # max(count.values()) is the count of the most frequent character in the window
            # So, the difference is the number of characters that need to be replaced
            while (r - l + 1) - max(count.values()) > k:
                # Reduce count of the character at the left pointer
                count[s[l]] -= 1
                # Move the left pointer to the right
                l += 1

            # Update the result with the maximum valid window size seen so far
            res = max(res, r - l + 1)

        return res