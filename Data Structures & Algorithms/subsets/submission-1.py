class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # This will store our final list of all subsets
        res = []
        
        # This will temporarily store the current subset we are building
        subset = []
        
        # Helper function to perform Depth-First Search (DFS)
        # 'i' represents the current index in 'nums' we are making a decision on
        def dfs(i):
            # Base Case: 
            # If our index 'i' has reached the length of the array, 
            # it means we have made a decision (include or exclude) for every single element.
            if i >= len(nums):
                # We append a COPY of 'subset' to 'res'. 
                # (If we didn't use .copy(), all items in 'res' would update 
                # every time 'subset' changes later in the code).
                res.append(subset.copy())
                return
            
            # --- DECISION 1: INCLUDE the current element ---
            # Add the current number to our subset
            subset.append(nums[i])
            # Move on to the next element in the array
            dfs(i + 1)

            # --- DECISION 2: EXCLUDE the current element ---
            # Undo the previous addition (this is the "backtracking" step).
            # We remove the element we just added so we can explore the path where it's NOT included.
            subset.pop()
            # Move on to the next element in the array, but this time without nums[i] in the subset
            dfs(i + 1)
        
        # Start the recursion process from the very first index (0)
        dfs(0)

        # Return the populated list of all subsets
        return res