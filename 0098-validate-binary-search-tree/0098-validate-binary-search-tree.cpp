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
        auto dfs = [](this auto&& self, TreeNode* node, long long left,
                      long long right) -> bool {
            // Return true if current node is empty because we have nothing to
            // check
            if (node == nullptr) {
                return true;
            }
            // Return false if current node is not valid for any of left/right
            // bounds
            if (!(node->val > left && node->val < right)) {
                return false;
            }
            return self(node->left, left, node->val) &&
                   self(node->right, node->val, right);
        };

        // Note that TreeNode's value is int so we're using `long long` to avoid
        // the boundary problem For example, if we use INT_MIN and if that
        // node's value is INT_MIN, the bool check will not return what we
        // expected. Thus, we use a wider range and guarantee to have 8 bytes in
        // all platforms, which is long long.
        return dfs(root, LLONG_MIN, LLONG_MAX);
    }
};