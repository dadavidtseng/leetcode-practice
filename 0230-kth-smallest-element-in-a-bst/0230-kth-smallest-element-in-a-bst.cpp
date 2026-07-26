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

        // Use inorder traversal for BST and push node's value into result as it
        // goes Note that result will be sorted naturally because of the nature
        // of BST
        auto dfs = [&](this auto&& self, TreeNode* node) -> void {
            if (node == nullptr) {
                return;
            }
            self(node->left);
            result.push_back(node->val);
            self(node->right);
        };

        dfs(root);

        // Return kth smallest element
        return result[k - 1];
    }
};