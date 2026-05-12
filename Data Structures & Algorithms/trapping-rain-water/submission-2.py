class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: If the array is empty, no water can be trapped.
        if not height:
            return 0

        # Initialize two pointers at the absolute ends of the elevation map.
        l, r = 0, len(height) - 1
        
        # Track the highest bars seen so far from the left and the right.
        leftMax, rightMax = height[l], height[r]
        
        # This will accumulate our total trapped water.
        res = 0
        
        # Process the terrain until the two pointers meet.
        while l < r:
            # The bottleneck determines how much water a column can hold. 
            # If leftMax < rightMax, we know the left side is the bottleneck for pointer 'l'.
            if leftMax < rightMax:
                # Move the left pointer inward.
                l += 1
                
                # Update the highest bar seen on the left.
                leftMax = max(leftMax, height[l])
                
                # Calculate trapped water at the new 'l' position.
                # If the current height is lower than leftMax, water pools on top of it.
                # If it's higher or equal, (leftMax - height[l]) evaluates to 0 (no water trapped).
                res += leftMax - height[l]
                
            # If rightMax is smaller than or equal to leftMax, the right side is the bottleneck.
            else:
                # Move the right pointer inward.
                r -= 1
                
                # Update the highest bar seen on the right.
                rightMax = max(rightMax, height[r])
                
                # Calculate trapped water at the new 'r' position.
                res += rightMax - height[r]
                
        return res