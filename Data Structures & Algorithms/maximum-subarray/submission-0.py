class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxSub tracks the highest sum we've seen so far.
        # We initialize it to the first element to handle cases where 
        # all numbers in the array are negative.
        maxSub = nums[0] 
        
        # curSum keeps track of the running sum of our current subarray.
        curSum = 0

        # Iterate through each number in the array one by one
        for num in nums:
            
            # If our running sum drops below zero, it becomes a "liability".
            # Adding a negative running sum to the next number will only make 
            # the next number smaller. So, we discard the previous subarray 
            # and reset our running sum to 0.
            if curSum < 0:
                curSum = 0
            
            # Add the current number to our running sum
            curSum += num
            
            # Update maxSub if our new running sum is greater than 
            # the highest sum we've recorded so far.
            maxSub = max(maxSub, curSum)
            
        # After checking all numbers, maxSub holds the largest possible sum
        return maxSub