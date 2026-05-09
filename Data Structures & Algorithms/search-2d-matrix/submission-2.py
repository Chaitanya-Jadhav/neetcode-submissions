class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the dimensions of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # --------------------------------------------------------
        # PHASE 1: Binary search to find the correct ROW
        # --------------------------------------------------------
        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2  # Find the middle row
            
            # If the target is greater than the largest element in the current row
            # (which is the last element), the target must be in a row below.
            if target > matrix[row][-1]:
                top = row + 1
                
            # If the target is less than the smallest element in the current row
            # (which is the first element), the target must be in a row above.
            elif target < matrix[row][0]:
                bot = row - 1
                
            # If it's neither strictly greater than the max nor strictly less than the min,
            # then the target must potentially reside IN this current row.
            else:
                break 
        
        # If the loop finished and top > bot, it means the target doesn't 
        # fall within the range of any row in the matrix.
        if not (top <= bot):
            return False
        
        # --------------------------------------------------------
        # PHASE 2: Binary search to find the TARGET within the identified row
        # --------------------------------------------------------
        row = (top + bot) // 2  # This is the row we identified in Phase 1
        
        l, r = 0, COLS - 1
        
        while l <= r:
            m = (l + r) // 2  # Find the middle column index
            
            # Target is larger than middle element, search the right half
            if target > matrix[row][m]:
                l = m + 1
                
            # Target is smaller than middle element, search the left half
            elif target < matrix[row][m]:
                r = r - 1
                
            # Target found!
            else:
                return True
                
        # If the loop finishes without returning True, the target is not in the matrix
        return False