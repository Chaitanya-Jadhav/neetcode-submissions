# Node class used in the Trie
class TrieNode:
    def __init__(self):
        # Dictionary to hold children nodes where key = character, value = TrieNode
        self.children = {}
        # Flag to indicate if this node marks the end of a valid word
        self.endOfword = False

# Trie (Prefix Tree) class for inserting, searching, and prefix checking of words
class PrefixTree:
    def __init__(self):
        # The root of the Trie is an empty TrieNode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start from the root node
        cur = self.root
        # Iterate over each character in the word
        for c in word:
            # If the character is not already a child of the current node, add it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to the next node (child)
            cur = cur.children[c]
        # After inserting all characters, mark the end of the word
        cur.endOfword = True

    def search(self, word: str) -> bool:
        # Start from the root node
        cur = self.root
        # Iterate over each character in the word
        for c in word:
            # If the character is not found among children, word doesn't exist
            if c not in cur.children:
                return False
            # Move to the next node
            cur = cur.children[c]
        # After processing all characters, check if it's the end of a valid word
        return cur.endOfword

    def startsWith(self, prefix: str) -> bool:
        # Start from the root node
        cur = self.root
        # Iterate over each character in the prefix
        for c in prefix:
            # If the character is not found among children, prefix doesn't exist
            if c not in cur.children:
                return False
            # Move to the next node
            cur = cur.children[c]
        # If all prefix characters are found, return True
        return True
