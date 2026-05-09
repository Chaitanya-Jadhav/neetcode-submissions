class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the numbers we've iterated over so far.
        # Format: { number_value: index_in_array }
        prevMap = {}  

        # Iterate through the array using enumerate to get both index (i) and value (n)
        for i, n in enumerate(nums):
            
            # Calculate what number we need to add to 'n' to reach the 'target'
            # Example: If target is 9 and current number is 2, diff needed is 7
            diff = target - n
            
            # Check if this required 'diff' is already in our dictionary
            if diff in prevMap:
                
                # If we found it, we have our pair! 
                # Return the index of the previously seen number and the current index
                return [prevMap[diff], i]
            
            # If the diff wasn't found, add the current number and its index to the dictionary.
            # We do this AFTER checking so we don't accidentally use the same element twice.
            prevMap[n] = i