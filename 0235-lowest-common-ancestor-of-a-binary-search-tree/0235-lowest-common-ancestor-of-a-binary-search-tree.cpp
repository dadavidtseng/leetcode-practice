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
        // Return empty if any of root, p, and q is empty
        if (root == nullptr || p == nullptr || q == nullptr) {
            return nullptr;
        }

        TreeNode* curr = root;

        while (curr != nullptr) {
            // If current node's value is greater than p's and q's value, go
            // left
            if (curr->val > p->val && curr->val > q->val) {
                curr = curr->left;
            }

            // If current node's value is less than p's and q's value, go right
            else if (curr->val < p->val && curr->val < q->val) {
                curr = curr->right;
            }

            // Return the lowest common ancestor
            else {

                return curr;
            }
        }

        // This will never be reached because we've already checked if root/p/q
        // are valid
        return nullptr;
    }
};