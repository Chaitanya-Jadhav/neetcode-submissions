class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Quick Check: If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # 2. Initialize Hash Maps to store character counts
        countS, countT = {}, {}

        # 3. Single pass: Build frequency maps for both strings simultaneously
        for i in range(len(s)):
            # .get(key, 0) handles cases where the character isn't in the dict yet
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        # 4. Compare Maps: In Python, == checks if keys and values match exactly
        return countS == countT