class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize an array of 0s with the same length as the input.
        # We use 0 as the default because if a day never gets a warmer temperature, 
        # the answer for that day should remain 0.
        res = [0] * len(temperatures)
        
        # This stack will keep track of days for which we haven't found a warmer day yet.
        # It will store pairs of data: (temperature, index_of_that_day)
        stack = []

        # Loop through the temperatures list, getting both the index (i) and the temperature (t)
        for i, t in enumerate(temperatures):
            
            # The Core Logic: 
            # While the stack is not empty AND the current day's temperature (t) 
            # is warmer than the temperature at the top of the stack (stack[-1][0])...
            while stack and t > stack[-1][0]:
                
                # ...it means we have finally found a warmer day for the day at the top of the stack!
                # Pop that past day off the stack since its waiting is over.
                stackT, stackInd = stack.pop()
                
                # Calculate how many days we waited. 
                # (Current Day Index) - (Past Day Index) = Days Waited.
                # Save this result in the 'res' array at the exact index of that past day.
                res[stackInd] = i - stackInd
            
            # After resolving any past days that this current day is warmer than,
            # we must add the current day to the stack so it can wait for its own warmer day.
            stack.append((t, i))
            
        # Return the fully populated array of waiting days
        return res