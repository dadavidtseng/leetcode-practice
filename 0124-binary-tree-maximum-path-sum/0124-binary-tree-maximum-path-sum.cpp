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

        auto dfs = [&](this auto&& self, const TreeNode* node) -> int {
            // return 0 if node is empty
            if (node == nullptr) {
                return 0;
            }

            // Get left/right from the best chain of the left/right subtree,
            // ignore if negative because it'll decrement the result
            const int left = max(self(node->left), 0);
            const int right = max(self(node->right), 0);

            // Update result if left + node's value + right is greater than
            // result
            result = max(result, left + node->val + right);

            // Return current node's value + whichever is greater among left and
            // right
            return node->val + max(left, right);
        };

        // Pass root into DFS call
        dfs(root);
        return result;
    }
};