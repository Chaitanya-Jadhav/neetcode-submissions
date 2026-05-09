class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l],heights[r]) * (r - l)
            maxA = max(area, maxA)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] > heights[l]:
                r += 1
            else:
                l += 1
        return maxA
            