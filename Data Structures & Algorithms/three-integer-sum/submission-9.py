class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # This will store all unique triplets that sum to 0
        res = []
        
        # Sort the array first
        # Why? 
        # 1. Makes it possible to use two pointers
        # 2. Helps easily skip duplicates
        nums.sort()

        # Iterate through the array
        # 'i' is the index
        # 'a' is the fixed first element of the triplet
        for i, a in enumerate(nums):
            
            # Skip duplicate values for 'a'
            # Prevents duplicate triplets in the result
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Two-pointer setup
            # l starts right after 'a'
            # r starts at the end of the array
            l, r = i + 1, len(nums) - 1
            
            # Move the two pointers toward each other
            while l < r:
                
                # Current triplet sum
                threeSum = a + nums[l] + nums[r]
                
                # If sum is too large, move right pointer left
                # (because array is sorted, moving left decreases sum)
                if threeSum > 0:
                    r -= 1
                
                # If sum is too small, move left pointer right
                # (moving right increases sum)
                elif threeSum < 0:
                    l += 1
                
                else:
                    # Found a valid triplet
                    res.append([a, nums[l], nums[r]])
                    
                    # Move both pointers inward
                    l += 1
                    r -= 1
                    
                    # Skip duplicate values for the second number
                    # Ensures unique triplets
                    # Important: check l < r to avoid index error
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res

# Time & Space Complexity
# Time complexity: O(n^2)
# Space complexity:
#         O(1) or O(n) extra space depending on the sorting algorithm.
#         O(m) space for the output list.

# Where m is the number of triplets and n is the length of the given array. 