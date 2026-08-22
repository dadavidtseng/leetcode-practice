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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        // Create preIdx and inIdx to keep track of where we are in preorder and
        // inorder
        int preIdx = 0;
        int inIdx = 0;

        // Note that we only care about preoder's size because we are building
        // the tree using preorder as boundary. For inorder, we use it to know
        // whether we should build left/right subtrees and that has nothing to
        // do with its size.
        const int preorderSize = static_cast<int>(preorder.size());

        TreeNode* dummy = new TreeNode(0);
        TreeNode* curr = dummy;

        // Exit the while loop when eith preIdx or inIdx equal or greater than
        // preorder's size
        while (preIdx < preorderSize && inIdx < preorderSize) {
            // 1. Create a new node and have this new node points to current
            // node's right
            // 2. Assign current node's right to the new node(create/pass the
            // thread!)
            // 3. Move current node to its right
            // 4. Increment preorder index
            TreeNode* newNode =
                new TreeNode(preorder[preIdx], nullptr, curr->right);
            curr->right = newNode;
            curr = curr->right;
            preIdx++;

            // Exit the while loop when current node's value is inorder[inIdx]
            // because that's the end of left subtree
            // 1. Create a new node and have this new node points to current
            // node
            // 2. Assign current node's left to the new node
            // 3. Move current node to its left
            // 4. Increment preorder index
            while (curr->val != inorder[inIdx]) {
                TreeNode* newNode =
                    new TreeNode(preorder[preIdx], nullptr, curr);
                curr->left = newNode;
                curr = curr->left;
                preIdx++;
            }

            // Increment inorder index so that inorder[inIdx] points to root
            // node's value
            inIdx++;

            // Exit the while loop when current node's right is empty or current
            // node's right vaule isn't root node in that subtree.
            // 1. Cache current node's right as root node using the thread we
            // created when building left subtree
            // 2. Remove the thread by assigning current node's right to empty
            // 3. Move current node back to root node(parent)
            // 4. Increment inorder index
            while (curr->right != nullptr &&
                   curr->right->val == inorder[inIdx]) {
                TreeNode* root = curr->right;
                curr->right = nullptr;
                curr = root;
                inIdx++;
            }
        }
        return dummy->right;
    }
};