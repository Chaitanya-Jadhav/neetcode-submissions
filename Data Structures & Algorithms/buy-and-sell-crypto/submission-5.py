class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = left pointer (buy day)
        # r = right pointer (sell day)
        l, r = 0, 1
        
        # maxP stores the maximum profit found so far
        maxP = 0

        # Traverse the list using the right pointer
        while r < len(prices):
            
            # If selling price is higher than buying price,
            # we can calculate a profit
            if prices[l] < prices[r]:
                
                # Calculate current profit
                profit = prices[r] - prices[l]
                
                # Update maximum profit if current profit is larger
                maxP = max(maxP, profit)
            
            else:
                # If current price is lower than buying price,
                # move left pointer to current day
                # (better buying opportunity)
                l = r
            
            # Move right pointer forward to check next day
            r += 1
        
        # Return the maximum profit found
        return maxP

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(1)

