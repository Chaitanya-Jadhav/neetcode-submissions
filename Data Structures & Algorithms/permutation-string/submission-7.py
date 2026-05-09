class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: If s1 is longer than s2, s2 cannot possibly contain a permutation of s1
        if len(s1) > len(s2):
            return False

        # Initialize two arrays of size 26 to store character frequencies for 'a' through 'z'
        s1Count, s2Count = [0] * 26, [0] * 26
        
        # Build the initial frequency maps for s1 and the first window in s2 (size of s1)
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Calculate the initial number of matching character frequencies between s1 and the first window of s2
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # 'l' is the left pointer of our sliding window
        l = 0
        
        # 'r' is the right pointer, starting right after the initial window
        for r in range(len(s1), len(s2)):
            # If all 26 characters have matching frequencies, we found a permutation!
            if matches == 26:
                return True

            # --- PROCESS THE NEW CHARACTER ENTERING THE WINDOW (Right side) ---
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            # If the frequency just became equal, we gained a match
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If it was equal before but we just added one, we lost a match
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # --- PROCESS THE OLD CHARACTER LEAVING THE WINDOW (Left side) ---
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            # If removing this character made the frequencies equal, we gained a match
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If it was equal before but we just removed one, we lost a match
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            
            # Slide the left pointer forward
            l += 1
            
        # Final check for the very last window after the loop finishes
        return matches == 26