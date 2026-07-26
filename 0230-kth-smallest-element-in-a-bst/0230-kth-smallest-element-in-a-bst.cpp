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
    int kthSmallest(TreeNode* root, int k) {
        vector<int> result;

        // Brutally traverse through the BST and store every node's values in
        // result
        auto dfs = [&](this auto&& self, TreeNode* node) -> void {
            if (node == nullptr) {
                return;
            }
            result.push_back(node->val);
            self(node->left);
            self(node->right);
        };

        dfs(root);

        // Sort result and return kth smallest element
        sort(result.begin(), result.end());
        return result[k - 1];
    }
};