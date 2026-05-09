class Solution:

    def encode(self, strs: List[str]) -> str:
        # Initialize an empty string to store the final encoded result
        res = ""
        
        # Iterate through each string in the input list
        for s in strs:
            # Format each string as: <length> + "#" + <string>
            # Example: "lint" becomes "4#lint"
            # This ensures that even if the string itself contains a "#", 
            # we know exactly how many characters to read later.
            res += str(len(s)) + "#" + s
            
        return res

    def decode(self, s: str) -> List[str]:
        # Initialize an empty list to store the decoded strings
        res = []
        
        # 'i' is our main pointer tracking our current position in the encoded string
        i = 0

        # Loop until we have processed the entire encoded string
        while i < len(s):
            # 'j' is a secondary pointer used to find the '#' delimiter
            j = i
            
            # Move 'j' forward until it hits the '#' character.
            # Everything between 'i' and 'j' represents the length of the upcoming string.
            while s[j] != '#':
                j += 1
                
            # Extract the length string (from i to j) and convert it to an integer
            length = int(s[i:j])
            
            # Move 'i' to the first character of the actual string (right after the '#')
            i = j + 1
            
            # Move 'j' to the index just after the end of the actual string
            j = i + length
            
            # Extract the actual string using slicing and add it to our result list
            res.append(s[i:j])
            
            # Update 'i' to point to the start of the next encoded string length
            i = j

        return res