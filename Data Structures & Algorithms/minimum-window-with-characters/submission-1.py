class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: If the target string is empty, no window can exist
        if t == "":
            return ""

        # countT: Frequency of characters required in string 't'
        # window: Frequency of characters currently in our sliding window
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # 'have' tracks how many unique characters in 't' meet the required frequency in the current window
        # 'need' is the total number of unique characters in 't' that we must satisfy
        have, need = 0, len(countT)
        
        # res stores the [left, right] indices of the best window found; resLen tracks the minimum length
        res, resLen = [-1, -1], float("infinity")
        l = 0
        
        # 'r' is the right pointer, expanding the window
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # If the current character is needed AND its count matches the requirement, increment 'have'
            if c in countT and window[c] == countT[c]:
                have += 1

            # While the current window contains all required characters (the condition is satisfied)
            while have == need:
                # Update our result if the current window is smaller than any previous one
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Try to shrink the window from the left to find an even smaller valid window
                window[s[l]] -= 1
                
                # If removing s[l] makes the window lose a required character count, decrement 'have'
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                # Move the left pointer forward
                l += 1
        
        # Extract the final indices and return the substring; return empty string if no window was found
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""