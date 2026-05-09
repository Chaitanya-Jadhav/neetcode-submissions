class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes. Keys are characters, values are TrieNode objects.
        self.children = {}
        # Boolean flag to mark if this specific node represents the end of a complete word.
        self.word = False

class WordDictionary:
    def __init__(self):
        # Initialize the Trie with an empty root node.
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root # Start traversing from the root
        
        for c in word:
            # If the character doesn't exist in the current node's children, create a new node.
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move the pointer down to the child node to process the next character.
            cur = cur.children[c]
            
        # Once all characters are inserted, mark the final node as the end of a valid word.
        cur.word = True

    def search(self, word: str) -> bool:
        # Helper function for Depth-First Search (DFS) to handle the "." wildcard.
        # 'j' is the current index in the word string; 'root' is the current TrieNode.
        def dfs(j, root):
            cur = root
            
            # Iterate through the word starting from index 'j'
            for i in range(j, len(word)):
                c = word[i]
                
                if c == ".":
                    # WILDCARD CASE: The "." can represent ANY character.
                    # We must explore every possible path (every child node) from here.
                    for child in cur.children.values():
                        # Recursively call dfs moving to the next character (i + 1).
                        # If ANY of these paths return True, we found a match.
                        if dfs(i + 1, child):
                            return True
                    # If we checked all children and none formed the target word, return False.
                    return False
                else:
                    # REGULAR CHARACTER CASE:
                    # If the exact character isn't a child, the word doesn't exist.
                    if c not in cur.children:
                        return False
                    # Otherwise, move the pointer to the child node.
                    cur = cur.children[c]
                    
            # After processing the whole string, check if we actually stopped at a word boundary.
            # (e.g., returns False if we searched for "app" but only "apple" is in the Trie).
            return cur.word
        
        # Start the recursive search at index 0 using the root of the Trie.
        return dfs(0, self.root)