class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is empty, return an empty string
        if t == "":
            return ""

        # Step 1: Count frequency of each character in t
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # `have` tracks how many characters have been satisfied
        # `need` is total unique characters required from t
        have, need = 0, len(countT)

        # `res` stores the start and end index of the minimum window
        # `resLen` is used to track the length of the smallest valid window found
        res, resLen = [-1, -1], float("infinity")
        l = 0  # Left pointer for sliding window

        # Step 2: Expand the window with the right pointer
        for r in range(len(s)):
            c = s[r]
            # Add the current character to the window count
            window[c] = 1 + window.get(c, 0)

            # If current character is needed and now matches the required count
            if c in countT and window[c] == countT[c]:
                have += 1

            # Step 3: Contract the window from the left if it's valid
            while have == need:
                # Update result if current window is smaller than previous best
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Remove the leftmost character from the window
                window[s[l]] -= 1

                # If that character is required and we no longer satisfy its count
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # Move the left pointer forward to shrink the window
                l += 1

        # Step 4: Return the result substring
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
