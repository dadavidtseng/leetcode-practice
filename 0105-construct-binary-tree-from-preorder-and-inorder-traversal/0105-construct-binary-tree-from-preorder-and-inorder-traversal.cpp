/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        const int inorderSize = static_cast<int>(inorder.size());
        int preIdx = 0;
        unordered_map<int, int> m;

        // Iterate through inorder to create inorder's value to index map
        for (int i = 0; i < inorderSize; ++i) {
            m[inorder[i]] = i;
        }

        // subtree's range= [L, R]
        auto dfs = [&](this auto&& self, int L, int R) -> TreeNode* {
            // Return empty when L crosses R
            if (L > R) {
                return nullptr;
            }

            // Get root node's value from preorder[preorder's index]
            // and then increment preorder's index
            int rootVal = preorder[preIdx++];

            // Create root node
            TreeNode* root = new TreeNode(rootVal);

            // Get the index of root node in inorder
            int M = m[rootVal];

            // inorder = (L, M - 1) | root | (M + 1, R)
            root->left = self(L, M - 1);
            root->right = self(M + 1, R);
            return root;
        };
        return dfs(0, inorderSize - 1);
    }
};