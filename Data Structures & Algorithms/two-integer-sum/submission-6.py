class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map to store 'value: index' pairs of numbers we have already seen
        # This allows O(1) average time complexity for lookups
        prevMap = {}  

        for i, n in enumerate(nums):
            # Calculate the 'complement' needed to reach the target
            diff = target - n
            
            # If the complement exists in our map, we found the pair
            if diff in prevMap:
                # Return the index of the complement and the current index
                return [prevMap[diff], i]
            
            # Otherwise, add current number and its index to the map for future checks
            prevMap[n] = i

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(n)