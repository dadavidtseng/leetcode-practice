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

        int result = 0;

        // Create a stack to store a pair of node and depth
        // and push the root node with depth 1 into the stack
        stack<pair<TreeNode*, int>> s;
        s.push({root, 1});

        // Exit the while loop when the stack is empty
        while (!s.empty()) {
            // Get the current node and depth from the stack
            const pair<TreeNode*, int> curr = s.top();
            s.pop();
            const TreeNode* node = curr.first;
            const int depth = curr.second;

            // If that node exists,
            //      1. Push that node's left/right children and incremented
            //      depth into the stack
            //      2. Calculate the max depth
            if (node != nullptr) {
                s.push({node->left, depth + 1});
                s.push({node->right, depth + 1});
                result = max(result, depth);
            }
        }
        return result;
    }
};