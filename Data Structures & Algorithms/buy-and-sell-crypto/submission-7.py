class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize two pointers: 
        # 'l' (left) is the day we BUY, starting at day 0.
        # 'r' (right) is the day we SELL, starting at day 1.
        l, r = 0, 1 
        
        # Track the maximum profit we have seen so far. 
        # It starts at 0 because if no profit is possible, we don't buy.
        maxP = 0

        # Loop through the array until the right pointer reaches the end
        while r < len(prices):
            
            # Check if the transaction is profitable (Sell price > Buy price)
            if prices[l] < prices[r]:
                # Calculate the profit for the current window
                profit = prices[r] - prices[l]
                
                # Update maxP if the current profit is higher than our previous best
                maxP = max(maxP, profit)
                
            else:
                # CRITICAL STEP: If prices[l] >= prices[r], it means we found a price
                # that is LOWER than our current buy price. 
                # We should shift our buy day (l) to this new lower price day (r) 
                # to maximize future potential profits.
                l = r
                
            # Regardless of what happened above, always move the right pointer
            # forward by 1 day to evaluate the next potential sell day.
            r += 1
            
        # After evaluating all possible windows, return the highest profit found
        return maxP