from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False  # Flag to check if the first row needs to be zeroed

        # 1️⃣ First pass: mark rows and columns that need to be zeroed
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # Mark the column in the first row
                    matrix[0][c] = 0
                    if r > 0:
                        # Mark the row in the first column
                        matrix[r][0] = 0
                    else:
                        # Special case: zero found in the first row
                        rowZero = True

        # 2️⃣ Second pass: use markers to set matrix cells to zero
        for r in range(1, rows):  # Skip the first row for now
            for c in range(1, cols):  # Skip the first column
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # 3️⃣ Zero out the first column if needed
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0  # ← (Fixed: use assignment, not comparison)

        # 4️⃣ Zero out the first row if `rowZero` is True
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
