from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0  # Variable to store the maximum water area found so far
        l, r = 0, len(heights) - 1  # Two-pointer approach: left and right ends of the array

        # Loop until the two pointers meet
        while l < r:
            # Calculate the area between the two pointers
            # Width is (r - l), height is the smaller of the two heights
            area = (r - l) * min(heights[l], heights[r])

            # Update the result if this area is larger than the current max
            res = max(res, area)

            # Move the pointer pointing to the shorter line inward
            # Because moving the taller one won’t help increase the area
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                # If both heights are equal, moving either pointer is valid; move right one here
                r -= 1

        # Return the maximum area found
        return res
