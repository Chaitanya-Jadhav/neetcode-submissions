class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        # Sort the candidates first. 
        # This is CRUCIAL for two reasons:
        # 1. It groups duplicates together so we can easily skip them later.
        # 2. It allows us to potentially break early if numbers get too large, 
        #    though this specific implementation just relies on the base cases.
        candidates.sort()

        def dfs(i, cur, total):
            # BASE CASE 1: Success
            # If our current combination sums up to the target, add it to results.
            if total == target:
                # We must append a COPY of cur (cur.copy()), because 'cur' is a 
                # reference to a list that we will keep modifying as we backtrack.
                res.append(cur.copy())
                return
            
            # BASE CASE 2: Failure / Out of bounds
            # If we exceeded the target, or we've run out of candidates to check, 
            # stop exploring this path.
            if total > target or i == len(candidates):
                return
            
            # --- DECISION 1: INCLUDE the current candidate ---
            # Add the current number to our combination
            cur.append(candidates[i])
            
            # Move to the next index (i + 1) because each number can only be used ONCE.
            # Update the running total.
            dfs(i + 1, cur, total + candidates[i])

            # BACKTRACKING STEP:
            # We finished exploring all paths that INCLUDED candidates[i]. 
            # Now, pop it off the list so we can explore paths that DO NOT include it.
            cur.pop()

            # --- DECISION 2: SKIP the current candidate ---
            # To avoid duplicate combinations in our final result, if we choose to skip 
            # the current number, we must also skip all identical numbers immediately following it.
            # (Because we already found all combinations involving this specific value above).
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            # Now recurse for the next UNIQUE number. Notice we use the updated 'i', 
            # and the 'total' remains the same since we didn't add the skipped numbers.
            dfs(i + 1, cur, total)

        # Start the Depth-First Search at index 0, with an empty current path, and a sum of 0
        dfs(0, [], 0)
        
        return res