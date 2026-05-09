class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty list to use as a stack
        stack = []
        
        # Map closing brackets to their corresponding opening brackets
        # This makes it easy to check for a match in O(1) time
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            # Check if the current character is a CLOSING bracket
            if c in closeToOpen:
                # 1. Ensure the stack isn't empty (an empty stack means no opening bracket exists)
                # 2. Check if the top of the stack matches the required opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # Match found! Remove the opening bracket from the stack
                else:
                    # If stack is empty or brackets don't match, the string is invalid
                    return False
            else:
                # If the character is an OPENING bracket, push it onto the stack
                stack.append(c)

        # After the loop, the string is only valid if the stack is completely empty
        # (meaning every opening bracket found its matching closing partner)
        return True if not stack else False