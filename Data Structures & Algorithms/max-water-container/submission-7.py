class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize two pointers:
        # l starts at the beginning, r starts at the end
        l, r = 0, len(heights) - 1
        
        # Variable to store the maximum area found so far
        res = 0

        # Continue until the two pointers meet
        while l < r:
            
            # The height of the container is limited by the shorter line
            # The width is the distance between the two pointers
            area = min(heights[l], heights[r]) * (r - l)
            
            # Update the maximum area if current area is larger
            res = max(res, area)

            # Move the pointer pointing to the shorter line inward
            # because moving the taller line cannot increase the area
            # (height is limited by the shorter one)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        # Return the maximum area found
        return res

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(1)
