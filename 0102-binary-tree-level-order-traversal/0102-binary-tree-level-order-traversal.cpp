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
        vector<vector<int>> result;

        auto dfs = [&](this auto&& self, TreeNode* node, int depth) -> void {
            // Return if current node is empty
            if (node == nullptr) {
                return;
            }

            // Push an empty container for this level if result's size equals
            // depth
            if (static_cast<int>(result.size()) == depth) {
                result.push_back(vector<int>{});
            }

            // Push current node's value into result[depth]
            result[depth].push_back(node->val);

            // Recursive call with left/right nodes and (depth+1)
            self(node->left, depth + 1);
            self(node->right, depth + 1);
        };

        dfs(root, 0);
        return result;
    }
};