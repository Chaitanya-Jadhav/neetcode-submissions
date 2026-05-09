class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Base Case: Anagrams must have the exact same number of characters.
        # If the lengths are different, they cannot be anagrams.
        if len(s) != len(t):
            return False
        
        # 2. Initialize two hash maps (dictionaries) to keep track of 
        # how many times each character appears in string 's' and string 't'.
        countS, countT = {}, {}

        # 3. Iterate through the indices of the strings. 
        # Since we already know s and t are the same length, we can use one loop for both.
        for i in range(len(s)):
            
            # For string 's':
            # Look at the character s[i]. Update its count in the dictionary.
            # .get(s[i], 0) looks for the character in the dict. If it's not there yet, it returns 0.
            # Then we add 1 to either the existing count or the 0.
            countS[s[i]] = 1 + countS.get(s[i], 0)
            
            # For string 't':
            # Do the exact same thing for the character at the same index in string 't'.
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        # 4. Finally, compare the two dictionaries. 
        # In Python, checking if dict1 == dict2 automatically checks if they have 
        # the exact same keys with the exact same values.
        return countS == countT