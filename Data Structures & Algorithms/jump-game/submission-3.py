class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the 'goal' as the last index of the array.
        # This is the final position we are trying to reach.
        goal = len(nums) - 1

        # Loop backwards through the array.
        # Start at the second-to-last index: len(nums) - 2
        # Stop at the first index: -1 (exclusive, so it stops at 0)
        # Step backwards by 1: -1
        for i in range(len(nums) - 2, -1, -1):
            
            # Check if the current position (i) plus the maximum jump distance 
            # from this position (nums[i]) can reach or overshoot the current goal.
            if i + nums[i] >= goal:
                
                # If we can reach the goal from index 'i', we don't need to worry 
                # about reaching the original goal anymore. We just need to reach 'i'.
                # So, we shift the goalpost closer to the start.
                goal = i
            
        # After checking all positions back to the start, if our goalpost 
        # has successfully moved all the way to index 0, it means we can 
        # jump from the start to the end.
        return goal == 0