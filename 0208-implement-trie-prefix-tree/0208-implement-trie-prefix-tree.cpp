class Trie {
public:
    Trie() = default;
    Trie(const Trie&) = delete;
    Trie& operator=(const Trie&) = delete;

    void insert(string word) {
        // Current root node in trie
        TrieNode* node = &root;

        // Iterate through the word string
        for (int i = 0; i < static_cast<int>(word.length()); i++) {
            const int idx = word[i] - 'a';

            // Create a new TrieNode if next node is empty
            if (node->children[idx] == nullptr) {
                node->children[idx] = new TrieNode();
            }

            // Advance to next node
            node = node->children[idx];
        }
        // We've finished inserting the nodes
        node->isEndOfWord = true;
    }

    bool search(string word) {
        TrieNode const* node = traverse(word);
        // Return false if we didn't find anything;
        // Return true if node is the end of the word, otherwise, it's just a
        // prefix
        return node == nullptr ? false : node->isEndOfWord;
    }

    bool startsWith(string prefix) { return traverse(prefix) != nullptr; }

private:
    struct TrieNode {
        TrieNode* children[26] = {nullptr};
        bool isEndOfWord = false;

        ~TrieNode() {
            for (int i = 0; i < 26; ++i) {
                delete children[i];
            }
        }
    };

    TrieNode* traverse(string const& word) {
        // Current root node in trie
        TrieNode* node = &root;

        // Iterate through the word string
        for (int i = 0; i < static_cast<int>(word.length()); ++i) {
            const int idx = word[i] - 'a';

            // Return empty if next node is empty,
            // which means that we failed to find the provided word
            if (node->children[idx] == nullptr) {
                return nullptr;
            }

            // Advance to next node
            node = node->children[idx];
        }
        // Return the node in Trie for the final char in word
        return node;
    }

    TrieNode root;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */