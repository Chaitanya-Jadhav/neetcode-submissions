class Solution:
    def checkValidString(self, s: str) -> bool:
        # leftMin tracks the minimum possible number of open left parentheses.
        # leftMax tracks the maximum possible number of open left parentheses.
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                # Exactly one '(' encountered. Both our minimum and maximum 
                # possible open parentheses increase.
                leftMin += 1
                leftMax += 1
                
            elif c == ")":
                # Exactly one ')' encountered. This closes an open parenthesis, 
                # so both our minimum and maximum decrease.
                leftMin -= 1
                leftMax -= 1
                
            else:
                # A '*' is encountered. It can act as ')', '', or '('.
                # If it acts as ')', our minimum open parentheses decreases.
                leftMin -= 1
                # If it acts as '(', our maximum open parentheses increases.
                leftMax += 1
            
            # If leftMax falls below 0, it means we have more closing brackets ')' 
            # than open brackets '(', even if we turned every single '*' into a '('.
            # The string is completely invalid.
            if leftMax < 0:
                return False
            
            # leftMin can't be negative. A negative leftMin just means we assumed 
            # too many '*' were ')' when we didn't need to. We can simply treat 
            # some of those '*' as empty strings instead, keeping leftMin at 0.
            if leftMin < 0:
                leftMin = 0
        
        # At the end, if leftMin is 0, it means there's a valid combination of 
        # choices for '*' that leaves us with exactly 0 unmatched open parentheses.
        return leftMin == 0