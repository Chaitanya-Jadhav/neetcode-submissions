from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []   # This will store all the valid palindrome partitions (list of lists)
        part = []  # This will store the current partition path we are exploring

        # Helper function for Depth-First Search (Backtracking)
        def dfs(i):
            # BASE CASE: 
            # If our starting index 'i' goes out of bounds, it means we have 
            # successfully partitioned the entire string into palindromes.
            if i >= len(s):
                # Append a COPY of the current partition to our results.
                # If we don't copy (part.copy()), future modifications to 'part' 
                # will alter the arrays already stored inside 'res'.
                res.append(part.copy())
                return
            
            # RECURSIVE STEP:
            # Try exploring all possible substrings starting from index 'i' to 'j'
            for j in range(i, len(s)):
                # Only proceed if the current substring s[i...j] is a palindrome
                if self.isPalindrom(s, i, j):
                    # 1. CHOOSE: Add the valid palindrome substring to our current path
                    part.append(s[i:j+1])
                    
                    # 2. EXPLORE: Recursively call dfs for the rest of the string, 
                    # starting from the very next character (j + 1)
                    dfs(j + 1)
                    
                    # 3. UN-CHOOSE (Backtrack): Remove the last added substring so 
                    # we can try the next 'j' in the loop (different substring length)
                    part.pop()
        
        # Start the backtracking process from the 0th index
        dfs(0)
        
        return res

    # Helper function to check if a substring is a palindrome using two pointers
    def isPalindrom(self, s, l, r):
        # Continue checking as long as the left pointer is before the right pointer
        while l < r:
            # If characters don't match, it's not a palindrome
            if s[l] != s[r]:
                return False
            # Move the pointers closer to the center
            l, r = l + 1, r - 1
            
        return True