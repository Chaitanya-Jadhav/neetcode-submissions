class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Store the dimensions of the board for easy access
        ROWS, COLS = len(board), len(board[0])
        
        # 'path' keeps track of the coordinates we are currently visiting in our DFS.
        # This prevents us from using the same letter cell more than once in a single word path.
        path = set()

        # Helper function to perform Depth-First Search
        # r = current row, c = current col, i = current index of the character we are looking for in 'word'
        def dfs(r, c, i):
            # BASE CASE 1: Success!
            # If our index 'i' has reached the length of the word, it means we have 
            # successfully found all characters in the correct order.
            if i == len(word):
                return True

            # BASE CASE 2: Failure / Out of Bounds!
            # We must stop exploring this path if any of the following are true:
            # 1. Row 'r' or Col 'c' is less than 0 (Out of bounds left/top)
            # 2. Row 'r' or Col 'c' is greater than or equal to the board limits (Out of bounds right/bottom)
            # 3. The character on the board does not match the character we need (word[i])
            # 4. We have already visited this exact cell in our current path
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            # If we pass the base cases, it means board[r][c] is a valid match for word[i].
            # Mark this cell as visited by adding its coordinates to our path set.
            path.add((r, c))
            
            # Recursively explore all 4 adjacent directions (Down, Up, Right, Left).
            # We look for the next character in the word by passing 'i + 1'.
            # 'res' will be True if ANY of these directional searches find the rest of the word.
            res = (dfs(r + 1, c, i + 1) or  # Go Down
                   dfs(r - 1, c, i + 1) or  # Go Up
                   dfs(r, c + 1, i + 1) or  # Go Right
                   dfs(r, c - 1, i + 1))    # Go Left
            
            # BACKTRACKING STEP:
            # Once we finish exploring all paths from this cell, we must remove it from the path set.
            # This allows other distinct paths starting from different initial cells to potentially 
            # use this cell again.
            path.remove((r, c))
            
            # Return whether we found the word along this path
            return res

        # Main execution: Iterate through every single cell on the board.
        # We treat every cell as a potential starting letter for our word.
        for r in range(ROWS):
            for c in range(COLS):
                # If a DFS starting from (r, c) looking for the 0th character returns True, we are done.
                if dfs(r, c, 0):
                    return True
                    
        # If we loop through the entire board and never return True, the word doesn't exist.
        return False