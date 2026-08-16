/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        auto dfs = [&](this auto&& self, TreeNode* node) -> TreeNode* {
            // If current node's value is greater than p's and q's value, go
            // left
            if (node->val > p->val && node->val > q->val) {
                return self(node->left);
            }

            // If current node's value is less than p's and q's value, go right
            if (node->val < p->val && node->val < q->val) {
                return self(node->right);
            }

            // Return the lowest common ancestor
            return node;
        };

        // Return empty if any of root, p, and q is empty
        if (root == nullptr || p == nullptr || q == nullptr) {
            return nullptr;
        }
        return dfs(root);
    }
};