class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(i, total):
            if total == n:
                return True
            
            if i > n:
                return False

            return 1 + int(dfs(i+1, total) or dfs(i+2, total))

        return dfs(1, 0)
