class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # A set to store the unique characters in our current "window".
        # Sets provide O(1) lookup time to quickly check for duplicates.
        charSet = set() 
        
        # 'l' is the left pointer of our sliding window.
        l = 0           
        
        # 'res' will keep track of the maximum length we've found so far.
        res = 0         

        # 'r' is the right pointer. It expands the window by iterating through the string.
        for r in range(len(s)):
            
            # If the character at the right pointer is already in our set, 
            # we have found a repeating character. Our current window is invalid.
            while s[r] in charSet:
                # To fix this, we shrink the window from the left.
                # We remove the character at the left pointer from the set...
                charSet.remove(s[l])
                # ...and move the left pointer forward.
                # This loop continues until the duplicate of s[r] is removed.
                l += 1
                
            # Now that the window is guaranteed to have no duplicates, 
            # we add the new character at the right pointer to our set.
            charSet.add(s[r])
            
            # Calculate the length of the current valid window: (right - left + 1)
            # Update 'res' if this new length is greater than our previous maximum.
            res = max(res, r - l + 1)
            
        # Return the longest valid substring length found.
        return res