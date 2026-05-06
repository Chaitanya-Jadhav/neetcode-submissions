class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Initialize boundaries for the outermost layer of the matrix
        left, right = 0, len(matrix) - 1
        
        # Keep processing layers as long as the left boundary is less than the right boundary.
        # (For a 3x3 matrix, it stops at the center element. For a 4x4, it stops after the inner 2x2).
        while left < right:
            
            # Iterate through the elements of the current layer.
            # 'offset' represents how far we are from the corners of the current layer.
            for offset in range(right - left):
                
                # Since the matrix is an NxN square, top and bottom boundaries 
                # map exactly to the left and right boundaries.
                top, bottom = left, right

                # STEP 1: Save the top-left value. 
                # We are about to overwrite it, so we need to store it temporarily.
                topLeft = matrix[top][left + offset]

                # STEP 2: Move the bottom-left element into the top-left position.
                # As 'offset' increases, we move DOWN the left edge.
                matrix[top][left + offset] = matrix[bottom - offset][left]

                # STEP 3: Move the bottom-right element into the bottom-left position.
                # As 'offset' increases, we move LEFT across the bottom edge.
                matrix[bottom - offset][left] = matrix[bottom][right - offset]

                # STEP 4: Move the top-right element into the bottom-right position.
                # As 'offset' increases, we move UP the right edge.
                matrix[bottom][right - offset] = matrix[top + offset][right]

                # STEP 5: Move the saved top-left element into the top-right position.
                # As 'offset' increases, we move RIGHT across the top edge.
                matrix[top + offset][right] = topLeft
            
            # Move the boundaries inward by 1 to process the next inner concentric layer
            left += 1
            right -= 1