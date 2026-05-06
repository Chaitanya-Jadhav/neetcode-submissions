class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        
        # Dictionary to map closing brackets to their corresponding opening brackets
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        # Iterate through each character in the string
        for c in s:
            
            # If the character is a closing bracket
            if c in closeToOpen:
                
                # Check if stack is not empty AND
                # top of stack matches the corresponding opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # Valid match → remove opening bracket from stack
                else:
                    return False  # Mismatch or empty stack → invalid string
            
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(c)
        
        # If stack is empty, all brackets were matched correctly
        # If not empty, there are unmatched opening brackets
        return True if not stack else False

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(n)

