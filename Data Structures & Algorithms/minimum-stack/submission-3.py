class MinStack:
    def __init__(self):
        # The main stack to store all elements
        self.stack = []
        # A secondary stack to keep track of the minimums
        # Each index i in minStack stores the minimum value in stack[0...i]
        self.minStack = []

    def push(self, val: int) -> None:
        # 1. Add the value to the actual data stack
        self.stack.append(val)
        
        # 2. Determine the new minimum:
        # If minStack is empty, the current value is the minimum.
        # Otherwise, compare the current value with the previous minimum (top of minStack).
        val = min(val, self.minStack[-1] if self.minStack else val)
        
        # 3. Push the (potentially updated) minimum onto the minStack
        self.minStack.append(val)

    def pop(self) -> None:
        # Since both stacks are kept in sync, we pop from both
        # This ensures the minStack always reflects the current state of the main stack
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the last element added to the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # The top of minStack always represents the minimum of the entire stack
        # This allows O(1) retrieval time
        return self.minStack[-1]