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
        // Return empty if any of preorder and inorder is empty
        // Note that this is the base case of DFS, not an early return
        if (preorder.empty() || inorder.empty()) {
            return nullptr;
        }

        // Create root node using preorder[0]
        // because index 0 in preorder will always be the root of a subtree
        TreeNode* root = new TreeNode(preorder[0]);

        // Find preorder[0] in inorder and get preorder[0]'s index in inorder
        // Note that iteratorA - iteratorB = the distance between iteratorA and
        // iteratorB Ex.  iteratorA is a position 3, iteratorB is at position
        // 0(begin()),
        //      iteratorA - iteratorB = 3 = iteratorA's index
        auto mid =
            find(inorder.begin(), inorder.end(), preorder[0]) - inorder.begin();

        // preorder = root | preLeft | preRight
        // inorder = inorderLeft | root | inorderLeft
        // Note that vector(_First, _Last) doesn't include _Last
        vector preLeft(preorder.begin() + 1, preorder.begin() + 1 + mid);
        vector preRight(preorder.begin() + 1 + mid, preorder.end());
        vector inLeft(inorder.begin(), inorder.begin() + mid);
        vector inRight(inorder.begin() + mid + 1, inorder.end());

        // Pass in preLeft, preRight, inLeft, inRight for recursive call
        root->left = buildTree(preLeft, inLeft);
        root->right = buildTree(preRight, inRight);
        return root;
    }
};