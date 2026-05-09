class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize a stack to keep track of the numbers (operands)
        stack = []
        
        # Iterate through each token in the list one by one
        for c in tokens:
            if c == "+":
                # For addition, order doesn't matter. 
                # Pop the top two numbers, add them, and push the result back.
                stack.append(stack.pop() + stack.pop())
                
            elif c == "-":
                # For subtraction, order matters.
                # The first popped element 'a' is the right operand.
                # The second popped element 'b' is the left operand.
                a, b = stack.pop(), stack.pop()
                stack.append(b - a) # Execute (left - right)
                
            elif c == "*":
                # For multiplication, order doesn't matter.
                # Pop the top two numbers, multiply them, and push the result back.
                stack.append(stack.pop() * stack.pop())
                
            elif c == "/":
                # For division, order matters. 
                # 'a' is the divisor (bottom), 'b' is the dividend (top).
                a, b = stack.pop(), stack.pop()
                
                # Note on division in Python: Standard floor division (//) truncates toward negative infinity.
                # RPN typically requires division to truncate toward zero.
                # Using int(float(b) / a) correctly handles negative numbers by truncating toward zero.
                stack.append(int(float(b) / a))
                
            else:
                # If the token is not an operator, it must be a number.
                # Convert the string to an integer and push it onto the stack.
                stack.append(int(c))
                
        # After evaluating all tokens, the final result is the only item left in the stack.
        return stack[0]