class TrieNode:
    def __init__(self):
        # A dictionary to hold the children nodes. Keys are characters, values are TrieNodes.
        self.children = {}
        # A boolean flag to mark if a complete word ends at this node.
        self.isWord = False

    def addWord(self, word):
        """Inserts a word into the Trie."""
        cur = self
        for c in word:
            # If the character is not already a child, create a new TrieNode for it.
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move the pointer to the child node.
            cur = cur.children[c]
        # Mark the end of the newly inserted word.
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build the Trie from the given list of words.
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        # Cache the dimensions of the board to avoid repeated function calls.
        ROWS, COLS = len(board), len(board[0])
        
        # Use a set for 'res' to automatically prevent duplicate words in the output.
        # Use a set for 'visit' to keep track of the current path and avoid reusing cells.
        res, visit = set(), set()

        def dfs(r, c, node, word):
            """
            Depth-First Search to explore the board.
            r, c: Current row and column coordinates.
            node: The current TrieNode we are at.
            word: The string built so far along this path.
            """
            # Base Case / Out of Bounds / Invalid Checks:
            # 1. Is the row out of bounds?
            # 2. Is the column out of bounds?
            # 3. Has this cell already been visited in the current path?
            # 4. Does the character at this cell NOT exist in the current Trie node's children?
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or (r, c) in visit or
                board[r][c] not in node.children
            ):
                return # Stop exploring this path; it's a dead end.
            
            # If we pass the checks, mark the current cell as visited.
            visit.add((r, c))
            
            # Move to the child node corresponding to the letter on the board.
            node = node.children[board[r][c]]
            
            # Append the letter to our current word path.
            word += board[r][c]
            
            # If we've reached a node that marks the end of a dictionary word, add it to results.
            # Notice we do NOT return here; we might find a longer word with the same prefix.
            if node.isWord:
                res.add(word)
            
            # Recursively explore all 4 adjacent directions (down, up, right, left).
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Backtracking Step:
            # We are done exploring all paths from this specific cell.
            # Remove it from the visited set so it can be used in different paths later.
            visit.remove((r, c))

        # Step 2: Initiate a DFS search starting from every single cell on the board.
        for r in range(ROWS):
            for c in range(COLS):
                # Start with the root of the Trie and an empty string.
                dfs(r, c, root, "")
        
        # Convert the resulting set of words back into a list before returning.
        return list(res)