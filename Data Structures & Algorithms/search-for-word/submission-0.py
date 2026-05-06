class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the number of rows and columns in the board
        ROWS, COLS = len(board), len(board[0])

        # This set keeps track of the path we're currently exploring to avoid revisiting cells
        path = set()

        # Depth-First Search function that explores the board recursively
        def dfs(r, c, i):
            # If we've matched all characters in the word, return True
            if i == len(word):
                return True

            # If out of bounds, character doesn't match, or cell already used in current path, return False
            if (
                r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or 
                (r, c) in path
            ):
                return False

            # Add the current cell to the path to mark it as visited
            path.add((r, c))

            # Explore all 4 directions: down, up, left, right
            res = (
                dfs(r + 1, c, i + 1) or  # Down
                dfs(r - 1, c, i + 1) or  # Up
                dfs(r, c - 1, i + 1) or  # Left
                dfs(r, c + 1, i + 1)     # Right
            )

            # Backtrack: remove the current cell from the path
            path.remove((r, c))

            # Return the result of the recursive search
            return res

        # Try to start the DFS from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                # If DFS from (r, c) finds the word, return True
                if dfs(r, c, 0):
                    return True

        # If no path matches the word, return False
        return False
