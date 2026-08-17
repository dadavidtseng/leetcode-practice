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
    vector<vector<int>> levelOrder(TreeNode* root) {
        // Return empty if root is empty
        if (root == nullptr) {
            return {};
        }

        vector<vector<int>> result;
        queue<TreeNode*> q;

        // Push root so the while loop can start
        q.push(root);

        // Exist when the queue is empty, which means that we've processed
        // everything
        while (!q.empty()) {
            // Cache the current level size from the queue
            // Note that we have to do this because q's size changes in the for
            // loop below
            const int levelSize = static_cast<int>(q.size());
            vector<int> level;

            // Iterate through the queue to process current level
            for (int i = 0; i < levelSize; ++i) {
                // Read the front node and push its value into level
                const TreeNode* front = q.front();
                level.push_back(front->val);

                // Push front node's children into queue if they exist
                if (front->left != nullptr) {
                    q.push(front->left);
                }
                if (front->right != nullptr) {
                    q.push(front->right);
                }

                // Remove the front node since we don't need it anymore
                q.pop();
            }

            // Push level into result because the level container
            // should now contain current level's nodes in right order
            result.push_back(level);
        }
        return result;
    }
};