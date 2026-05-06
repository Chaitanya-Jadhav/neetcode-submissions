class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1     # Get the last integer and add it to res
                             # if 0 res remains same and if 1 res increments by 1 
            n = n >> 1       # shift n to the right by one
        return res