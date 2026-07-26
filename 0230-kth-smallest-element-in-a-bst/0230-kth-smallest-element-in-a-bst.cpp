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
        int result = 0;

        // Use inorder traversal for BST and decrement k as it goes
        // Note that result will be sorted naturally because of the nature of
        // BST
        auto dfs = [&](this auto&& self, TreeNode* node) -> void {
            if (node == nullptr || k == 0) {
                return;
            }
            self(node->left);

            if (k == 0) {
                return;
            }

            // 1. Decrement k
            // 2. Assign node's value to result
            // 3. Return from DFS
            k--;

            if (k == 0) {
                result = node->val;
                return;
            }
            self(node->right);
        };

        dfs(root);

        // Return kth smallest element
        return result;
    }
};