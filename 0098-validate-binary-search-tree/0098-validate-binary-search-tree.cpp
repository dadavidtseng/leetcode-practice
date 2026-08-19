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
    bool isValidBST(TreeNode* root) {
        auto isValid = [&](this auto&& self, TreeNode* node, const int limit,
                           const bool isLeft) -> bool {
            // Return true if current node is empty because we have nothing to
            // check
            if (node == nullptr) {
                return true;
            }

            // Compare differently based on the bool flag
            bool valid = isLeft ? node->val < limit : node->val > limit;

            // Return false if invalid
            if (!valid) {
                return false;
            }
            return self(node->left, limit, isLeft) &&
                   self(node->right, limit, isLeft);
        };
        auto dfs = [&](this auto&& self, TreeNode* node) {
            // Return true if current node is empty because we have nothing to
            // check
            if (node == nullptr) {
                return true;
            }
            // Return false if any of the recursive call returns false
            if (!isValid(node->left, node->val, true) ||
                !isValid(node->right, node->val, false)) {
                return false;
            }
            return self(node->left) && self(node->right);
        };
        return dfs(root);
    }
};