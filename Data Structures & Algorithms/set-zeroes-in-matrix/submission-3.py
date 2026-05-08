class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Get the dimensions of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # We need a separate flag for the first row. 
        # Why? Because matrix[0][0] will be used to track if the *first column* 
        # needs to be zeroed. We can't use it for both the first row and first column.
        rowZero = False

        # STEP 1: First pass to find zeroes and set our markers
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # Mark the top of the column to indicate this column should be zeroed
                    matrix[0][c] = 0

                    # Mark the start of the row to indicate this row should be zeroed
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        # If the zero is in the first row, we update our special flag instead
                        rowZero = True
        
        # STEP 2: Second pass to actually zero out the inner matrix
        # We skip the first row and first column (start at index 1) 
        # so we don't overwrite our markers prematurely.
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # If either the row marker or column marker is 0, set the cell to 0
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # STEP 3: Zero out the first column if needed
        # matrix[0][0] tells us if the first column needs to be completely zeroed
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # STEP 4: Zero out the first row if needed
        # Our special flag tells us if the first row needs to be completely zeroed
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0