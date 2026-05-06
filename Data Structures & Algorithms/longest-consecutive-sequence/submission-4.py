class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to set for O(1) lookups
        # This removes duplicates and allows fast existence checks
        numSet = set(nums)
        
        # Stores the length of the longest consecutive sequence found
        longest = 0

        # Iterate through each unique number
        for num in numSet:
            
            # Only start counting if 'num' is the beginning of a sequence
            # A number is a sequence start if (num - 1) does NOT exist
            # This avoids recounting sequences multiple times
            if (num - 1) not in numSet:
                
                # Current sequence length (at least 1 because num exists)
                length = 1
                
                # Keep checking consecutive numbers (num + 1, num + 2, ...)
                # Increase length while the next consecutive number exists
                while (num + length) in numSet:
                    length += 1
                
                # Update the longest sequence found so far
                longest = max(length, longest)
        
        # Return the maximum consecutive sequence length
        return longest