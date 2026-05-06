class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get number of rows and columns
        ROWS, COLS = len(matrix), len(matrix[0])

        # We will binary search to find the correct row first
        top, bot = 0, ROWS - 1

        # Binary search over rows
        while top <= bot:
            row = (top + bot) // 2  # Middle row index

            # If target is greater than the last element of this row,
            # then target must be in a lower row
            if target > matrix[row][-1]:
                top = row + 1

            # If target is smaller than the first element of this row,
            # then target must be in a higher row
            elif target < matrix[row][0]:
                bot = row - 1

            # Target must exist within this row's range
            else:
                break
        
        # If we exited the loop without finding a valid row
        if not (top <= bot):
            return False
        
        # We now perform binary search within the selected row
        row = (top + bot) // 2
        l, r = 0, COLS - 1

        # Standard binary search on the row
        while l <= r:
            m = (l + r) // 2  # Middle column index

            # If target is larger, search right half
            if target > matrix[row][m]:
                l = m + 1

            # If target is smaller, search left half
            # (NOTE: This should technically be r = m - 1 for correct binary search)
            elif target < matrix[row][m]:
                r = r - 1

            # Target found
            else:
                return True

        # Target not found
        return False

# Time & Space Complexity
# Time complexity: O(log⁡m+log⁡n) (which reduces to O(log⁡(m∗n)))
# Space complexity: O(1)
#
# Where m is the number of rows and n is the number of columns of matrix.