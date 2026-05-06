class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        # Initialize the four boundaries. 
        # Note: 'right' and 'bottom' are initialized as out-of-bounds indices (the lengths), 
        # so we will use right - 1 and bottom - 1 when accessing elements.
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # Keep spiraling inward as long as our boundaries haven't crossed.
        # This means there is still a valid sub-matrix to process.
        while left < right and top < bottom:
            
            # 1. Move LEFT to RIGHT along the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            # The current top row is fully visited, so shrink the top boundary downwards
            top += 1
            
            # 2. Move TOP to BOTTOM along the rightmost column
            for i in range(top, bottom):
                # Using right - 1 because 'right' was initialized as len(matrix[0])
                res.append(matrix[i][right - 1])
            # The current right column is fully visited, so shrink the right boundary leftwards
            right -= 1

            # CRITICAL CHECK: Have the boundaries crossed after the first two steps?
            # If the matrix is not a perfect square (e.g., it's a 1D row or column at this point),
            # we need to break out early so we don't traverse backward and duplicate elements.
            if not (left < right and top < bottom):
                break
            
            # 3. Move RIGHT to LEFT along the bottom row
            # range(start, stop, step): starts at right-1, goes down to 'left', counting by -1
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            # The current bottom row is fully visited, so shrink the bottom boundary upwards
            bottom -= 1
            
            # 4. Move BOTTOM to TOP along the leftmost column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            # The current left column is fully visited, so shrink the left boundary rightwards
            left += 1
        
        return res