class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to group anagrams.
        # The key will be a tuple representing the character count of each word.
        res = defaultdict(list)

        # Iterate through each string in the input list
        for s in strs:
            # Initialize a count array for 26 lowercase letters (a–z)
            count = [0] * 26

            # Count the frequency of each character in the current string
            for c in s:
                count[ord(c) - ord("a")] += 1

            # Use the character count tuple as a key to group anagrams
            # Strings with the same character frequency will have the same key
            res[tuple(count)].append(s)

        # Return the grouped anagrams as a list of lists
        return res.values()