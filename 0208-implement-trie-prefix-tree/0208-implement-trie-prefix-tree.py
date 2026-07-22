class Trie:
    class TrieNode:
        def __init__(self):
            self.children: dict[str, Trie_Prefix_Tree_Hash_Map.TrieNode | None] = {}
            self.is_end_of_word = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = self.TrieNode()
            node = node.children[c]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.__traverse(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        return self.__traverse(prefix) is not None

    def __traverse(self, word: str) -> "TrieNode | None":
        node = self.root

        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node
