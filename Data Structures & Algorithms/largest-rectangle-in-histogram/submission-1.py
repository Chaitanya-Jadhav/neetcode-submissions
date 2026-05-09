class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        
        # The stack will store pairs of (index, height).
        # 'index' represents the furthest left index this 'height' can stretch to.
        stack = []  

        for i, h in enumerate(heights):
            start = i # Initially, assume the current bar starts at its own index
            
            # If the stack is not empty AND the current height is shorter than the 
            # height at the top of the stack...
            # This means the taller bar at the top of the stack cannot extend any 
            # further to the right. We must calculate its max area now.
            while stack and stack[-1][1] > h:
                # Pop the taller bar from the stack
                index, height = stack.pop()
                
                # Calculate the area. The width is the current index (i) minus the 
                # index where the popped bar started.
                # Update maxArea if this new area is larger.
                maxArea = max(maxArea, height * (i - index))
                
                # CRITICAL STEP: Since the current shorter bar (h) can stretch backwards 
                # through the space of the taller bar we just popped, we update its 
                # starting index to the popped bar's index.
                start = index
            
            # Add the current bar to the stack with its (potentially extended) starting index
            stack.append((start, h))

        # After going through all bars, some might still be left in the stack.
        # These are bars that can extend all the way to the right edge of the histogram.
        for i, h in stack:
            # The width is the total length of the histogram minus the starting index.
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea