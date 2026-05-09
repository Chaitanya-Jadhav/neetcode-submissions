class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to store the frequency of characters in the current window
        count = {}
        # Stores the length of the longest valid substring found so far
        res = 0

        # 'l' is the left pointer of our sliding window
        l = 0
        # 'maxf' keeps track of the count of the most frequent character in the window
        maxf = 0
        
        # 'r' is the right pointer, iterating through the string to expand the window
        for r in range(len(s)):
            # Add the current character at the right pointer to our frequency map
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # Update the maximum frequency we've seen in the window.
            # (Note: even if the window shrinks later, keeping the historical maxf is safe 
            # because we only care about finding a window LARGER than our current 'res')
            maxf = max(maxf, count[s[r]])

            # Check if the current window is invalid.
            # Window size is (r - l + 1). 
            # (Window size) - (count of most frequent character) = Number of characters we need to replace.
            # If this number is greater than our allowed replacements (k), the window is invalid.
            while (r - l + 1) - maxf > k:
                # The window is invalid, so we need to shrink it from the left.
                # Decrease the frequency of the character at the left pointer
                count[s[l]] -= 1
                # Move the left pointer forward
                l += 1
            
            # Update the result with the maximum valid window size found so far
            res = max(res, r - l + 1)
            
        return res