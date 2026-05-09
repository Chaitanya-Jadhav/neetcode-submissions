class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # Step 1: Sort the array. 
        # Sorting is crucial because it allows us to use the two-pointer technique 
        # and makes it easy to skip duplicate values to avoid duplicate triplets.
        nums.sort()

        # Step 2: Iterate through the array. 
        # 'a' represents the first number of our potential triplet.
        for i, a in enumerate(nums):
            
            # Optimization & Duplicate check for the 1st number:
            # If the current number is the same as the previous one, skip it.
            # We already explored all possible triplets starting with this number.
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Step 3: Initialize two pointers.
            # 'l' (left) starts right after our fixed element 'a'.
            # 'r' (right) starts at the very end of the sorted array.
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                # Calculate the sum of the current triplet
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    # If the sum is too large, we need a smaller number.
                    # Since the array is sorted, moving the right pointer leftward decreases the sum.
                    r -= 1
                    
                elif threeSum < 0:
                    # If the sum is too small, we need a larger number.
                    # Moving the left pointer rightward increases the sum.
                    l += 1
                    
                else:
                    # We found a valid triplet that sums to zero!
                    res.append([a, nums[l], nums[r]])
                    
                    # Move both pointers to search for the next potential triplet 
                    # with the same first number 'a'.
                    l += 1
                    r -= 1
                    
                    # Duplicate check for the 2nd number (left pointer):
                    # While the new left pointer points to the same value as the old left pointer,
                    # keep moving it to the right to avoid adding duplicate triplets to our result.
                    # (We also must ensure l < r so the pointers don't cross).
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
                    # Note: We don't strictly need a duplicate check loop for the right pointer 
                    # because the left pointer duplicate check combined with the strict 
                    # 'threeSum == 0' condition naturally prevents adding identical triplets.
                    
        return res