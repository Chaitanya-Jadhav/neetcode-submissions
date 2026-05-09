class MinStack:
    """
    A stack data structure that supports pushing, popping, top, and 
    retrieving the minimum element in constant O(1) time.
    """
    
    def __init__(self):
        # The main stack that stores all the pushed values in order.
        self.stack = []
        
        # A parallel stack that keeps track of the minimum value 
        # at the corresponding level of the main stack.
        self.minStack = []

    def push(self, val: int) -> None:
        # Always push the new value onto the main stack.
        self.stack.append(val)
        
        # Determine the current minimum value:
        # If minStack is not empty, compare the new 'val' with the current minimum 
        # (which is at the top of minStack, i.e., self.minStack[-1]).
        # If minStack is empty, the new 'val' is naturally the minimum.
        current_min = min(val, self.minStack[-1] if self.minStack else val)
        
        # Push this current minimum onto the minStack so it stays in sync 
        # with the main stack's height.
        self.minStack.append(current_min)

    def pop(self) -> None:
        # Remove the top element from the main stack.
        self.stack.pop()
        
        # We must also remove the top element from the minStack to keep 
        # both stacks perfectly synced. The new top of minStack will now 
        # correctly reflect the minimum of the remaining elements.
        self.minStack.pop()

    def top(self) -> int:
        # Return the last added element from the main stack without removing it.
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the last added element from the minStack. 
        # Because of how we push, this is always the smallest number 
        # currently in the main stack.
        return self.minStack[-1]