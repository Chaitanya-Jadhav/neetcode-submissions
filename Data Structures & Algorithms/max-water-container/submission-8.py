class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize two pointers: 
        # 'l' at the start (left edge) and 'r' at the end (right edge) of the array.
        l, r = 0, len(heights) - 1
        
        # 'res' will store the maximum area found so far.
        res = 0

        # Loop until the two pointers meet in the middle.
        while l < r:
            # Calculate the area with the current left and right pointers.
            # 1. min(heights[l], heights[r]) determines the bottleneck height (water spills over the shorter side).
            # 2. (r - l) calculates the width between the two lines.
            area = min(heights[l], heights[r]) * (r - l)
            
            # Update 'res' if the newly calculated area is larger than our previous maximum.
            res = max(res, area)

            # Move the pointer that points to the shorter line inward.
            # Why? Because bringing the pointers closer together always DECREASES the width.
            # To have any chance of finding a larger area, we MUST find a taller line.
            # Moving the taller line inward won't help because the height is bounded by the shorter line.
            if heights[l] < heights[r]:
                l += 1  # The left line is shorter, move the left pointer rightward
            else:
                r -= 1  # The right line is shorter (or equal), move the right pointer leftward
                
        # Return the absolute maximum area found after checking all potential bounds.
        return res