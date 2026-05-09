class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # This will hold all of our final valid string combinations
        res = []

        # A hash map connecting each digit to its corresponding phone keypad letters
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        # The backtracking helper function
        # i: represents our current index in the 'digits' string
        # curStr: represents the current combination of letters we are building
        def backtrack(i, curStr):
            # BASE CASE: 
            # If the string we built is the same length as the input digits string, 
            # we have a complete combination. Add it to our results and stop going deeper.
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            # RECURSIVE STEP:
            # 1. digits[i] gets the current number we are looking at (e.g., "2")
            # 2. digitToChar[...] gets the letters for that number (e.g., "abc")
            for c in digitToChar[digits[i]]:
                # Move to the next digit (i + 1) and add the current letter (c) to our string
                backtrack(i + 1, curStr + c)
        
        # Edge Case: We only want to start the recursion if the input string is not empty.
        # If 'digits' is "", we skip this and just return the empty 'res' list.
        if digits:
            # Kick off the recursion starting at index 0 with an empty string
            backtrack(0, "")

        return res