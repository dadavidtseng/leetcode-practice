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
        // Return true if root is empty
        if (root == nullptr) {
            return true;
        }

        // Create a queue that carries current node and left/right bounds
        // and push root into the queue so we can start the while loop
        queue<tuple<TreeNode*, long long, long long>> q;
        q.push(make_tuple(root, LLONG_MIN, LLONG_MAX));

        // Exit the while loop when queue is empty
        while (!q.empty()) {
            // Get the front node and remove it from the queue
            auto [node, left, right] = q.front();
            q.pop();

            // Continue is current node is empty because we don't need to
            // process it
            if (node == nullptr) {
                continue;
            }

            // Return false if current node is not valid for any of left/right
            // bounds
            if (!(node->val > left && node->val < right)) {
                return false;
            }

            q.push(make_tuple(node->left, left, node->val));
            q.push(make_tuple(node->right, node->val, right));
        }

        // Return true if we've successfully processed all nodes in the BST
        return true;
    }
};