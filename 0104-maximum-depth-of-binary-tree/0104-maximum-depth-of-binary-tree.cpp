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
    int maxDepth(TreeNode* root) {
        // Return 0 if the root is nullptr
        if (root == nullptr) {
            return 0;
        }

        // Recursively compute the depth of the left/right subtrees and add 1
        // for each of them
        const int leftDepth = 1 + maxDepth(root->left);
        const int rightDepth = 1 + maxDepth(root->right);

        // Return the maximum from left/right depths as we unwind
        return max(leftDepth, rightDepth);
    }
};