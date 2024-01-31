# Insert and Search in a Trie

class TrieNode: 
      
    def __init__(self): 
        self.children = [None] * 26
        self.isEndOfWord = False

class Solution:
    # Function to insert a string into TRIE.
    def insert(self, root, key):
        current = root

        for char in key:
            index = ord(char) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]

        current.isEndOfWord = True

    # Function to use TRIE data structure and search the given string.
    def search(self, root, key):
        current = root

        for char in key:
            index = ord(char) - ord('a')
            if not current.children[index]:
                return False
            current = current.children[index]

        return current.isEndOfWord

# Example usage:
trie_root = TrieNode()
solution = Solution()

# Inserting strings into the Trie
solution.insert(trie_root, "apple")
solution.insert(trie_root, "app")

# Searching for strings in the Trie
print(solution.search(trie_root, "apple"))
