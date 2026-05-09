class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l].lower() != s[r].lower():
                print(s[l],s[r])
                return False
            l, r = l + 1, r - 1
            return True