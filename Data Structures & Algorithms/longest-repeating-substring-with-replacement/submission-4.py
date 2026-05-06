class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to store frequency of characters in current window
        count = {}
        
        # Result: stores the maximum valid window length found
        res = 0

        # Left pointer of sliding window
        l = 0
        
        # maxf keeps track of the frequency of the most common character 
        # in the current window
        maxf = 0
        
        # Expand the window using right pointer
        for r in range(len(s)):
            
            # Increase frequency of current character
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # Update max frequency seen in the window
            maxf = max(maxf, count[s[r]])

            # If number of characters to change > k, shrink window
            # Window size = (r - l + 1)
            # Characters to replace = window size - max frequency
            while (r - l + 1) - maxf > k:
                
                # Remove left character from window
                count[s[l]] -= 1
                
                # Move left pointer forward (shrink window)
                l += 1
            
            # Update result with the largest valid window size
            res = max(res, r - l + 1)

        # Return maximum length of substring after at most k replacements
        return res

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(m)
# Where n is the length of the string and m is the total number of unique characters in the string. 