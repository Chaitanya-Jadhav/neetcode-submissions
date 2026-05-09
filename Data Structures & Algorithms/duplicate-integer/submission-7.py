class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Step 1: Sort the array. 
        # This groups any identical elements together. 
        # Time complexity of sorting in Python is O(n log n).
        nums.sort()
        
        # Step 2: Iterate through the sorted array.
        # We start at index 1 so we can safely compare the current 
        # element (nums[i]) with the previous element (nums[i - 1]).
        for i in range(1, len(nums)):
            
            # Step 3: Check for adjacent duplicates.
            # If the current number is the same as the one right before it, 
            # we have found a duplicate.
            if nums[i] == nums[i - 1]:
                return True
                
        # Step 4: No duplicates found.
        # If the loop finishes checking all elements without returning True, 
        # it means every number in the array is unique.
        return False