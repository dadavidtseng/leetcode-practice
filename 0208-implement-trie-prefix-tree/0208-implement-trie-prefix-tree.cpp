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
            const char c = word[i];

            // Create a new TrieNode if next node is empty
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }

            // Advance to next node
            node = node->children[c];
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
        unordered_map<char, TrieNode*> children;
        bool isEndOfWord = false;

        ~TrieNode() {
            for (auto it = children.begin(); it != children.end(); ++it) {
                delete it->second;
            }
        }
    };

    TrieNode* traverse(const string& word) {
        // Current root node in trie
        TrieNode* node = &root;

        // Iterate through the word string
        for (int i = 0; i < static_cast<int>(word.length()); ++i) {
            const char c = word[i];

            // Return empty if next node is empty,
            // which means that we failed to find the provided word
            if (node->children.find(c) == node->children.end()) {
                return nullptr;
            }

            // Advance to next node
            node = node->children[c];
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