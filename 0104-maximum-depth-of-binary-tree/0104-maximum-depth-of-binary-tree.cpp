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

        // Create a queue to store nodes from root
        // and push the root node into the queue
        queue<TreeNode*> q;
        q.push(root);

        // Exit the while loop when the queue is empty
        while (!q.empty()) {
            const int size = static_cast<int>(q.size());

            // Iterate through every nodes in the queue,
            // which is the nodes in a level
            for (int i = 0; i < size; ++i) {
                // Get the node from the queue,
                // which is the very left node for this level
                // if this is the first iteration of the for loop
                const TreeNode* node = q.front();
                q.pop();

                // Push that node's left child into the queue if it exists
                if (node->left != nullptr) {
                    q.push(node->left);
                }

                // Push that node's right child into the queue if it exists
                if (node->right != nullptr) {
                    q.push(node->right);
                }
            }
            // Increment the result as we finished a level
            result++;
        }
        return result;
    }
};