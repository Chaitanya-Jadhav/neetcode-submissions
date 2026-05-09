from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Dictionaries where the values are sets. 
        # Using sets gives us O(1) time complexity for lookups/checking if a number exists.
        cols = defaultdict(set)    # Key: column index (0-8)
        rows = defaultdict(set)    # Key: row index (0-8)
        squares = defaultdict(set) # Key: tuple of (row_box_index, col_box_index)

        # Iterate through every cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                # If the cell is empty, skip to the next iteration
                if board[r][c] == ".":
                    continue
                
                # Check if the current number has already been seen in its row, column, or 3x3 box.
                # r // 3 and c // 3 map the 0-8 indices to a 0-2 index for the 3x3 sub-boxes.
                # Example: rows 0, 1, 2 all become 0. Rows 3, 4, 5 become 1. Rows 6, 7, 8 become 2.
                if (board[r][c] in cols[c] 
                    or board[r][c] in rows[r]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    # A duplicate was found, so the board is invalid
                    return False
                
                # If it's a new number, add it to our tracking sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        # If we successfully check every cell without returning False, the board is valid
        return True