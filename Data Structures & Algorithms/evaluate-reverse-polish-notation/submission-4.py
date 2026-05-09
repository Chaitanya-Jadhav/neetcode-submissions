class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty stack to keep track of numbers
        stack = []
        
        for c in tokens:
            # Multiplicative and Additive operations are commutative, 
            # so the order of popped elements doesn't change the result.
            if c == "*":
                stack.append(stack.pop() * stack.pop())
                
            elif c == "+":
                stack.append(stack.pop() + stack.pop())
                
            # Division and Subtraction are NOT commutative.
            # The first element popped is the RIGHT operand (a), 
            # and the second element popped is the LEFT operand (b).
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                # In Python, 'int(b / a)' truncates toward zero, 
                # which is the behavior required by most LeetCode/RPN problems.
                stack.append(int(b / a))
                
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                # We must subtract the first popped value from the second.
                stack.append(b - a)
                
            else:
                # If the token is not an operator, it's a number.
                # Convert the string to an integer and push it onto the stack.
                stack.append(int(c))
        
        # After processing all tokens, the final result is the only item left in the stack.
        return stack.pop()