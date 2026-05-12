class Solution:
    def jump(self, nums: List[int]) -> int:
        # res keeps track of the total number of jumps made
        res = 0
        
        # l (left) and r (right) represent the boundaries of the current "window" 
        # of indices we can reach with the current number of jumps.
        # Initially, at 0 jumps, we can only reach index 0.
        l = r = 0

        # Continue jumping until our window's right edge reaches or passes the last index
        while r < len(nums) - 1:
            # farthest will store the maximum index we can reach from the current window
            farthest = 0
            
            # Check every index within the current window [l, r]
            for i in range(l, r + 1):
                # i + nums[i] represents the farthest index reachable from the current index i.
                # We update 'farthest' to keep the absolute maximum reach across the entire window.
                farthest = max(farthest, i + nums[i])
            
            # Move to the next window for the next jump:
            # The next window starts right after the current window ends
            l = r + 1
            
            # The next window ends at the farthest point we just calculated we could reach
            r = farthest
            
            # We have just processed all possibilities for the current jump, 
            # so we increment our jump counter
            res += 1
            
        return res