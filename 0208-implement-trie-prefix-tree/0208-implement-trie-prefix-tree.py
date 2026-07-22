class Trie:
    """
    Note:
        Time:   O(n)
        Space:  O(t)
        Where n is the length of the string and t is the total number of TrieNodes created in the
        Trie.
    """

    class TrieNode:
        def __init__(self):
            self.children: dict[str, Trie_Prefix_Tree_Hash_Map.TrieNode | None] = {}
            self.is_end_of_word = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        # Current root node in trie
        node = self.root

        # Iterate through the word string
        for c in word:
            # Create a new TrieNode if next node is empty
            if c not in node.children:
                node.children[c] = self.TrieNode()

            # Advance to next node
            node = node.children[c]

        # We've finished inserting the nodes
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.__traverse(word)
        # Return false if we didn't find anything;
        # Return true if node is the end of the word, otherwise, it's just a prefix
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        return self.__traverse(prefix) is not None

    def __traverse(self, word: str) -> "TrieNode | None":
        # Current root node in trie
        node = self.root

        # Iterate through the word string
        for c in word:
            # Return empty if next node is empty,
            # which means that we failed to find the provided word
            if c not in node.children:
                return None

            # Advance to next node
            node = node.children[c]

        # Return the node in Trie for the final char in word
        return node
