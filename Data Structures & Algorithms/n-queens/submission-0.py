class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Sets to track which columns and diagonals currently have a Queen.
        # We use sets because checking if an item exists in a set is an O(1) operation.
        col = set()
        
        # Positive diagonals (/) go from bottom-left to top-right.
        # Every square on the same positive diagonal shares the same (row + col) value.
        posDiag = set() 
        
        # Negative diagonals (\) go from top-left to bottom-right.
        # Every square on the same negative diagonal shares the same (row - col) value.
        negDiag = set() 

        res = [] # This will store all our valid board configurations.
        
        # Initialize an n x n board filled with "." (representing empty spaces).
        board = [["."] * n for i in range(n)]

        # Recursive backtracking function. 
        # 'r' represents the current row we are trying to place a Queen in.
        def backtrack(r):
            # BASE CASE: If 'r' reaches 'n', we have successfully placed a Queen in every row.
            if r == n:
                # The board is currently a list of lists. We need to join the inner lists
                # into strings to match the expected List[List[str]] output format.
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # RECURSIVE STEP: Try placing a Queen in every column 'c' of the current row 'r'.
            for c in range(n):
                # Check if the current square (r, c) is under attack.
                # If its column, positive diagonal, or negative diagonal is already in our sets, skip it.
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                # --- 1. PLACE THE QUEEN (Make a choice) ---
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                # --- 2. RECURSE (Explore that choice) ---
                # Move on to the next row to place the next Queen.
                backtrack(r+1)

                # --- 3. BACKTRACK (Undo the choice) ---
                # We've explored all possibilities from that choice. 
                # Now, remove the Queen so the loop can try placing it in the next column.
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
        # Start the backtracking process at row 0.
        backtrack(0)

        return res