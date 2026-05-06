class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty stack to store numbers
        stack = []
        
        # Iterate through each token in the input list
        for c in tokens:
            
            # If the token is multiplication
            if c == "*":
                # Pop the top two numbers, multiply them,
                # and push the result back onto the stack
                stack.append(stack.pop() * stack.pop())
            
            # If the token is addition
            elif c == "+":
                # Pop the top two numbers, add them,
                # and push the result back onto the stack
                stack.append(stack.pop() + stack.pop())
            
            # If the token is division
            elif c == "/":
                # Important: Order matters in division
                # First pop is the second operand (a)
                # Second pop is the first operand (b)
                a, b = stack.pop(), stack.pop()
                
                # Perform division and truncate toward zero
                # int(b / a) ensures truncation instead of floor division
                stack.append(int(b / a))
            
            # If the token is subtraction
            elif c == "-":
                # Order matters in subtraction
                # First pop is the second operand (a)
                # Second pop is the first operand (b)
                a, b = stack.pop(), stack.pop()
                
                # Compute b - a and push result back
                stack.append(b - a)
            
            # If the token is a number
            else:
                # Convert string to integer and push onto stack
                stack.append(int(c))
        
        # Final result will be the only element left in the stack
        return stack.pop()

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(n)
