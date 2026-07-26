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
        TreeNode* curr = root;
        stack<TreeNode*> s;

        // Exit the loop when current node is empty and the stack is empty
        while (curr != nullptr || !s.empty()) {
            // Exit the loop when current node is nullptr,
            // otherwise, push the current node into stack
            // and keep going left
            while (curr != nullptr) {
                s.push(curr);
                curr = curr->left;
            }

            // 1. Get current node from the top of the stack
            // 2. Remove the visited node since we don't need it anymore
            // 3. Decrement k
            curr = s.top();
            s.pop();
            k--;

            // If k is 0, that mean we've reached our goal, return the current
            // node's value
            if (k == 0) {
                return curr->val;
            }

            // Move the current node to its right
            curr = curr->right;
        }
        // Return -1 to satisfy the compiler
        // Note that we'll never reach this because 1 <= k <= n <= 10^4
        return -1;
    }
};