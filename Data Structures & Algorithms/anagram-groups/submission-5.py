class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a dictionary where the default value for any new key is an empty list.
        # This prevents KeyErrors when we try to append to a key we haven't seen before.
        # It will map our character counts (the key) to a list of matching strings (the values).
        res = defaultdict(list)

        # Iterate through every string provided in the input array
        for s in strs:
            # Create a frequency array of 26 zeros, one for each lowercase letter in the alphabet ('a' through 'z').
            # We will use this to count how many times each letter appears in the current string 's'.
            count = [0] * 26
            
            # Iterate through each character in the current string
            for c in s:
                # Calculate the index for the character using its ASCII value.
                # ord(c) gets the ASCII value of the character.
                # Subtracting ord('a') maps 'a' to index 0, 'b' to 1, 'c' to 2, all the way to 'z' at 25.
                # We then increment the count at that specific index by 1.
                count[ord(c) - ord('a')] += 1
            
            # In Python, dictionary keys must be immutable (unhashable). 
            # Since 'count' is a list (which is mutable), we must convert it into a tuple first.
            # All anagrams will have the exact same tuple of character counts, so they will be appended to the same key.
            res[tuple(count)].append(s)
        
        # res.values() returns all the lists of grouped anagrams.
        # We wrap it in list() to match the required return type: List[List[str]].
        return list(res.values())