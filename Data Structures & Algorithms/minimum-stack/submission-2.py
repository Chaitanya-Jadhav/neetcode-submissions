class MinStack:
    """
    Stack that supports:
    - push
    - pop
    - top
    - retrieving the minimum element in constant time (O(1))
    
    Uses two stacks:
    1. Stack     -> stores all values
    2. minStack  -> stores the minimum value at each level
    """

    def __init__(self):
        # Main stack to store all pushed values
        self.Stack = []
        
        # Auxiliary stack to track the minimum value
        # minStack[i] = minimum of Stack[0:i+1]
        self.minStack = []

    def push(self, val: int) -> None:
        """
        Push a value onto the stack.
        
        We:
        1. Add val to the main stack.
        2. Compute the new minimum:
           - If minStack is empty → val is the minimum.
           - Otherwise → compare val with current minimum.
        3. Push the updated minimum onto minStack.
        """
        
        # Push value to main stack
        self.Stack.append(val)

        # Determine new minimum
        # If minStack exists, compare with current min
        # Otherwise, val is the minimum
        val = min(val, self.minStack[-1] if self.minStack else val)

        # Push the updated minimum to minStack
        self.minStack.append(val)

    def pop(self) -> None:
        """
        Remove the top element from the stack.
        
        Since both stacks grow together,
        we must pop from BOTH stacks to keep them aligned.
        """

        self.Stack.pop()      # Remove top from main stack
        self.minStack.pop()   # Remove corresponding minimum

    def top(self) -> int:
        """
        Return the top element of the main stack
        without removing it.
        """
        return self.Stack[-1]

    def getMin(self) -> int:
        """
        Return the current minimum element.
        
        The top of minStack always stores
        the minimum of the entire stack.
        """
        return self.minStack[-1]

# Time & Space Complexity
# Time complexity: O(1) for all operations.
# Space complexity: O(n)