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
        const int preorderSize = static_cast<int>(preorder.size());
        int preIdx = 0;
        int inIdx = 0;

        auto dfs = [&](this auto&& self, optional<int> limit) -> TreeNode* {
            // Return empty if we've processed all elements in preorder
            if (preIdx >= preorderSize) {
                return nullptr;
            }
            // If there's a limit and the value of that limit equals current
            // element in inorder
            // 1. Increment inorder's index
            // 2. Return empty
            if (limit && *limit == inorder[inIdx]) {
                inIdx++;
                return nullptr;
            }

            // Get root node's value from preorder[preorder's index]
            // and then increment preorder's index
            int rootVal = preorder[preIdx++];

            // Create root node
            TreeNode* root = new TreeNode(rootVal);

            // Pass in new limit for left/right subtrees for DFS call
            root->left = self(rootVal);
            root->right = self(limit);
            return root;
        };
        // Start the DFS call with no limit
        return dfs(nullopt);
    }
};