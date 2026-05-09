class TrieNode:
    """Represents a single node within the Trie."""
    def __init__(self):
        # Maps a character to its corresponding child TrieNode (e.g., {'a': TrieNode()})
        self.children = {} 
        # A flag to mark if this specific node is the final character of an inserted word
        self.endofword = False 

class PrefixTree:
    """The main Trie data structure."""
    def __init__(self):
        # The root is initialized as an empty TrieNode. 
        # It doesn't hold a character itself, but acts as the starting point for all paths.
        self.root = TrieNode() 
        
    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        cur = self.root
        
        for c in word:
            # If the current character is not a path from the current node, create one.
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            # Move the pointer down to the child node to process the next character.
            cur = cur.children[c]
            
        # Once the loop finishes, 'cur' is at the last character of the word.
        # We mark this node to signify a complete word ends here.
        cur.endofword = True

    def search(self, word: str) -> bool:
        """Returns True if the exact word exists in the trie, False otherwise."""
        cur = self.root
        
        for c in word:
            # If at any point the next letter isn't in the children, the word doesn't exist.
            if c not in cur.children:
                return False
            
            # Traverse down the tree.
            cur = cur.children[c]
            
        # We found the path for the word, but we must check if it was actually inserted 
        # or if it's just a prefix of another longer word. 
        # (e.g., searching for "app" when only "apple" was inserted should return False).
        return cur.endofword

    def startsWith(self, prefix: str) -> bool:
        """Returns True if any inserted word in the trie starts with the given prefix."""
        cur = self.root
        
        for c in prefix:
            # If the prefix path breaks at any point, no words start with this prefix.
            if c not in cur.children:
                return False
            
            # Traverse down the tree.
            cur = cur.children[c]
            
        # If we successfully traversed the entire prefix without returning False, 
        # it means the prefix exists in the tree. We don't care if it's a full word or not.
        return True