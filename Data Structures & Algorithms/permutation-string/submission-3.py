class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, it's impossible for s2 to contain a permutation of s1
        if len(s1) > len(s2):
            return False
        
        # Arrays to count frequency of characters in s1 and the current window of s2
        s1Count, s2Count = [0] * 26, [0] * 26

        # Populate the frequency arrays for s1 and the first window of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Count how many character frequencies match between s1Count and s2Count
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        # Initialize left pointer of sliding window
        l = 0

        # Slide the window through s2, starting from index len(s1)
        for r in range(len(s1), len(s2)):
            # If all 26 character counts match, a permutation is found
            if matches == 26:
                return True

            # --- Add new character to the window (right side) ---
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            # Update matches if frequency now matches or broke a previous match
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:  # was matching before, now doesn't
                matches -= 1

            # --- Remove old character from the window (left side) ---
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            # Update matches if frequency now matches or broke a previous match
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:  # was matching before, now doesn't
                matches -= 1
            
            # Move the left end of the window forward
            l += 1
        
        # Final check after the loop in case last window is valid
        return matches == 26
