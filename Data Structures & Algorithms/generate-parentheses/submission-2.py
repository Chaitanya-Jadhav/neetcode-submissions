class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 'stack' builds the current valid string of parentheses character by character.
        stack = []
        # 'res' stores all the completed, valid combinations to return at the end.
        res = []

        # The backtracking function keeps track of how many open and closed parentheses we've used so far.
        def backtrack(openN, closedN):
            # BASE CASE: A valid combination is found.
            # If the number of open and closed parentheses both equal 'n', our string is complete.
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # RULE 1: We can ADD AN OPEN parenthesis '(' as long as we haven't reached 'n'.
            if openN < n:
                stack.append("(")                  # 1. Choose: Add '(' to our current string.
                backtrack(openN + 1, closedN)      # 2. Explore: Move forward with one more open parenthesis.
                stack.pop()                        # 3. Backtrack: Remove '(' so we can try other paths.
            
            # RULE 2: We can ADD A CLOSED parenthesis ')' ONLY IF there are more open ones than closed ones.
            # This ensures we never close a parenthesis that hasn't been opened yet.
            if closedN < openN:
                stack.append(")")                  # 1. Choose: Add ')' to our current string.
                backtrack(openN, closedN + 1)      # 2. Explore: Move forward with one more closed parenthesis.
                stack.pop()                        # 3. Backtrack: Remove ')' so we can try other paths.
        
        # Start the recursion with 0 open and 0 closed parentheses.
        backtrack(0, 0)
        
        return res