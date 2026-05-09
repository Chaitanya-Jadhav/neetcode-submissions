class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set. 
        # This is the most crucial step for performance, as checking if an item 
        # exists in a set takes O(1) time, compared to O(n) for a list.
        numSet = set(nums)
        
        # Initialize a variable to keep track of the maximum length found so far.
        longest = 0

        # Iterate through the unique numbers in the set
        for num in numSet:
            # OPTIMIZATION TRICK: Check if this number is the START of a sequence.
            # If (num - 1) is in the set, then 'num' is just somewhere in the middle 
            # of a sequence, so we skip it to avoid redundant counting.
            if (num - 1) not in numSet:
                
                # If it is the start of a sequence, initialize the current length to 1
                length = 1
                
                # Keep checking if the next consecutive number exists in the set
                while (num + length) in numSet:
                    length += 1 # Increment the length for every consecutive number found
                
                # Update the 'longest' variable if the current sequence is longer 
                # than the previous longest sequence
                longest = max(length, longest)
        
        # Return the maximum length found after checking all sequences
        return longest