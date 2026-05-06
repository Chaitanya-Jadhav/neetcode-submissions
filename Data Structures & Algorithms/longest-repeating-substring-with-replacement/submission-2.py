class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
        maxF = 0 # why maxF
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            while (r - l + 1) - maxF > k: # This condition has the main crux
                count[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))

        return res