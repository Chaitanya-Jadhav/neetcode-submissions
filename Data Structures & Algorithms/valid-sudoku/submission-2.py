class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Dictionary mapping column index -> set of numbers seen in that column
        cols = defaultdict(set)
        
        # Dictionary mapping row index -> set of numbers seen in that row
        rows = defaultdict(set)
        
        # Dictionary mapping (subgrid_row, subgrid_col) -> set of numbers seen in that 3x3 square
        # Example: (0,0) = top-left square, (1,2) = middle-right square
        squares = defaultdict(set)

        # Iterate through every cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                
                # Skip empty cells
                if board[r][c] == ".":
                    continue
                
                # Check if current number already exists in:
                # 1. Current column
                # 2. Current row
                # 3. Current 3x3 subgrid
                if (
                    board[r][c] in cols[c] or
                    board[r][c] in rows[r] or
                    board[r][c] in squares[(r // 3, c // 3)]
                ):
                    # If duplicate found, Sudoku is invalid
                    return False
                
                # If valid, record the number in corresponding sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        # If no duplicates found after checking entire board
        return True