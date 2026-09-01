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
    int maxPathSum(TreeNode* root) {
        // return 0 if root node is empty
        if (root == nullptr) {
            return 0;
        }

        // Initialize the result to INT_MIN for all negative nodes case
        // Note that this could be result = -1001 because -1000 <= Node.val <=
        // 1000
        int result = INT_MIN;

        auto getMax = [](this auto&& self, const TreeNode* node) -> int {
            // return 0 if current node is empty
            if (node == nullptr) {
                return 0;
            }

            // Get left/right nodes from recursive call
            const int left = self(node->left);
            const int right = self(node->right);

            // Return current node's value + max(left, right) if current sum is
            // positive
            return max(node->val + max(left, right), 0);
        };

        auto dfs = [&](this auto&& self, const TreeNode* node) -> void {
            // return if node is empty
            if (node == nullptr) {
                return;
            }

            // Get left/right from current nodes' left/right subtrees
            const int left = getMax(node->left);
            const int right = getMax(node->right);

            // Update result if left + root's value + right is greater than
            // result
            result = max(result, left + node->val + right);

            // Pass in current node's left/right nodes into DFS call
            self(node->left);
            self(node->right);
        };

        // Pass root into DFS call
        dfs(root);
        return result;
    }
};