class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. Sort the list to bring identical elements next to each other
        # Time: O(n log n) | Space: O(1) or O(n) depending on sort implementation
        nums.sort()
        
        # 2. Iterate through the list starting from the second element
        for i in range(1, len(nums)):
            # 3. Compare current element with the previous one
            if nums[i] == nums[i - 1]:
                return True # Found a neighbor that is identical
        
        # 4. If the loop finishes without a match, all elements are unique
        return False