class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets
        stack = []
        
        # Map each closing bracket to its corresponding opening bracket
        # This makes lookups O(1) and the code much cleaner
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            # Check if the current character is a closing bracket
            if c in closeToOpen:
                # 1. 'stack' ensures we actually have an opening bracket to match
                # 2. 'stack[-1]' checks if the last opened bracket matches the current closer
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # Match found! Remove the opening bracket from the stack
                else:
                    # Either stack is empty (no opener) or it's the wrong type of opener
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(c)

        # If the stack is empty, all brackets were matched correctly.
        # If not empty, some brackets were opened but never closed.
        return True if not stack else False