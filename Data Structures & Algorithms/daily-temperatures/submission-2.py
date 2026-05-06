class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result list with 0s.
        # Each index will store how many days to wait for a warmer temperature.
        # Default is 0 because if no warmer day exists, answer stays 0.
        res = [0] * len(temperatures)
        
        # Stack to keep track of temperatures.
        # Each element in stack is a tuple: (temperature, index)
        # This is a MONOTONIC DECREASING stack (temps decreasing from bottom to top).
        stack = []

        # Iterate through the list with both index and temperature
        for i, t in enumerate(temperatures):
            
            # While:
            # 1. Stack is not empty
            # 2. Current temperature is warmer than the temperature at top of stack
            # This means we've found a warmer day for the previous day(s)
            while stack and t > stack[-1][0]:
                
                # Pop the previous colder temperature
                stackT, stackInd = stack.pop()
                
                # Calculate how many days we waited
                # Current index - previous index
                res[stackInd] = i - stackInd
            
            # Push current temperature and its index onto the stack
            # It may find a warmer day later
            stack.append((t, i))
        
        # Return the final result array
        return res

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(n)
