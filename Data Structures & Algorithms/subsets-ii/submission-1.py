class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # Step 1: Sort the array. 
        # This is CRITICAL for handling duplicates. Sorting ensures that all 
        # duplicate numbers are adjacent to each other, making them easy to skip.
        nums.sort()

        def backtrack(i, subset):
            # Base Case: We have considered every element in the input array.
            if i == len(nums):
                # We append a COPY of the subset [subset.copy() or subset[:]] 
                # because `subset` is a reference. If we don't copy it, future
                # modifications to `subset` will change what's already in `res`.
                res.append(subset.copy())
                return

            # --- DECISION 1: INCLUDE the current element nums[i] ---
            # Add the current number to our growing subset.
            subset.append(nums[i])
            # Move on to the next index.
            backtrack(i + 1, subset)

            # --- DECISION 2: EXCLUDE the current element nums[i] ---
            # To explore the path where we DON'T include nums[i], we must 
            # first remove it from our current subset (this is the "backtrack" step).
            subset.pop()

            # Since we chose to exclude nums[i], we must also exclude all future 
            # occurrences of this exact same number to prevent duplicate subsets.
            # We advance our index 'i' past any adjacent duplicates.
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                
            # Now we continue exploring down the exclusion path, starting from 
            # the next DIFFERENT number.
            backtrack(i + 1, subset)
        
        # Start the backtracking process at index 0 with an empty subset.
        backtrack(0, [])
        return res