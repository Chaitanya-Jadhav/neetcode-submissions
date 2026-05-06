class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to store unique characters in the current window
        charSet = set()
        
        # Left pointer of the sliding window
        l = 0
        
        # Variable to store the maximum length found so far
        res = 0

        # Right pointer expands the window
        for r in range(len(s)):
            
            # If duplicate character is found,
            # shrink the window from the left
            # until the duplicate is removed
            while s[r] in charSet:
                charSet.remove(s[l])  # Remove left character
                l += 1                # Move left pointer right
            
            # Add current character to the set
            charSet.add(s[r])
            
            # Update maximum length
            # Window length = r - l + 1
            res = max(res, r - l + 1)
        
        # Return the longest substring length without repeating characters
        return res

#Time & Space Complexity
#Time complexity: O(n)
#Space complexity: O(m)
#
#Where n is the length of the string and m is the total number of unique characters in the string. 

