class Solution:
    
    # Encodes a list of strings to a single string
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Add the length of the string, followed by '#', then the string itself
            # This ensures that decoding knows exactly how many characters to read
            res += str(len(s)) + "#" + s
        return res

    # Decodes a single string back into a list of strings
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the '#' to determine the boundary between length and actual string
            while s[j] != '#':
                j += 1
            
            # Extract the length of the next string
            length = int(s[i:j])
            
            # Move past the '#' to get to the actual string content
            i = j + 1

            # Extract the substring of given length
            j = i + length
            res.append(s[i:j])

            # Move the pointer to the start of the next encoded string
            i = j
            
        return res