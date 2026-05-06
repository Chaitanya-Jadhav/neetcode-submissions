class Solution:

    def encode(self, strs: List[str]) -> str:
        # This will store the final encoded string
        res = ""
        
        # Iterate through each string in the input list
        for s in strs:
            # For each string:
            # 1. Add its length
            # 2. Add a delimiter '#'
            # 3. Add the actual string
            # Format: "<length>#<string>"
            res += str(len(s)) + "#" + s
        
        # Return the fully encoded string
        return res

    def decode(self, s: str) -> List[str]:
        # This will store the decoded list of strings
        res = []
        
        # Pointer to track our position in the encoded string
        i = 0

        # Continue until we reach the end of the encoded string
        while i < len(s):
            
            # Find the position of the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length of the next string
            # (substring from i up to j, not including '#')
            length = int(s[i:j])
            
            # Move i to the start of the actual string
            i = j + 1
            
            # The string spans 'length' characters after '#'
            j = i + length
            
            # Extract the actual string and add it to result
            res.append(s[i:j])
            
            # Move i to the start of the next encoded segment
            i = j

        # Return the decoded list
        return res

# Time & Space Complexity
# Time complexity: O(m) for each encode() and decode() function calls.
# Space complexity: O(m+n) for each encode() and decode() function calls.

# Where m is the sum of lengths of all the strings and n is the number of strings. 