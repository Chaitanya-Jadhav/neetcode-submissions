class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, it is impossible for s2 to contain
        # a permutation of s1
        if len(s1) > len(s2):
            return False
        
        # Create frequency arrays for s1 and the current window in s2
        # We use size 26 because we assume lowercase English letters
        s1Count = [0] * 26
        s2Count = [0] * 26

        # Initialize the frequency counts for:
        # 1) Entire s1
        # 2) First window of s2 with size len(s1)
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # Count how many character frequencies match between s1Count and s2Count
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        # Left pointer of sliding window
        l = 0
        
        # Start sliding the window across s2
        # r is the right pointer of the window
        for r in range(len(s1), len(s2)):

            # If all 26 characters match in frequency,
            # we found a permutation
            if matches == 26:
                return True
            
            # ---- Add new character on the right ----
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            # If after incrementing, frequencies match -> increase matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If previously matched but now exceeded by 1 -> decrease matches
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            # ---- Remove character on the left ----
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            # If after decrementing, frequencies match -> increase matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If previously matched but now short by 1 -> decrease matches
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            
            # Move left pointer forward
            l += 1
        
        # Final check after loop ends
        return matches == 26
