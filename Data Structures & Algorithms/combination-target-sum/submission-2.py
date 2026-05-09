class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # This will store all of our successful combinations
        res = []

        # Helper function to perform Depth-First Search (Backtracking)
        # i: the current index in 'nums' we are looking at
        # cur: the current list of numbers we have chosen so far
        # total: the sum of the numbers inside 'cur'
        def dfs(i, cur, total):
            # BASE CASE 1: Success!
            # If our current total perfectly matches the target, we found a valid combination.
            if total == target:
                # We MUST append a copy of the list. If we just append 'cur', 
                # later modifications to 'cur' (like the pop() below) will alter the result inside 'res'.
                res.append(cur.copy())
                return
            
            # BASE CASE 2: Failure!
            # If we went out of bounds of the array OR our total exceeded the target, stop exploring.
            if i >= len(nums) or total > target:
                return

            # RECURSIVE STEP 1: Include the current number
            cur.append(nums[i])
            # We call dfs again with the SAME index 'i' because we are allowed 
            # to choose the same number an unlimited number of times.
            # We update the total by adding nums[i].
            dfs(i, cur, total + nums[i])

            # RECURSIVE STEP 2: Skip the current number
            # This is the "backtracking" step. We undo the choice we made above.
            cur.pop()
            # We call dfs again, but this time we move to the NEXT index (i + 1).
            # This branch explores all combinations that DO NOT include nums[i] anymore.
            dfs(i + 1, cur, total)
        
        # Initialize the DFS: start at index 0, with an empty combination list, and a total of 0.
        dfs(0, [], 0)

        return res