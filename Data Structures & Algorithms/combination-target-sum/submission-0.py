class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # This list will store all the valid combinations that sum to the target
        res = []

        # Helper function for depth-first search
        # i: current index in nums
        # cur: current combination being built
        # total: current sum of elements in cur
        def dfs(i, cur, total):
            # If the current total matches the target, we've found a valid combination
            if total == target:
                # Make a copy of the current combination and add it to the result
                res.append(cur.copy())
                return
            
            # If we've reached the end of the list or the current sum exceeds the target,
            # we stop exploring this path
            if i >= len(nums) or total > target:
                return
            
            # Include nums[i] in the current combination
            cur.append(nums[i])
            # Recurse with the same index to allow repeated use of the same number
            dfs(i, cur, total + nums[i])
            # Backtrack by removing the last number added
            cur.pop()
            # Recurse with the next index to explore combinations without the current number
            dfs(i + 1, cur, total)
        
        # Start the depth-first search with initial index 0, empty combination, and total sum 0
        dfs(0, [], 0)
        # Return all the valid combinations found
        return res