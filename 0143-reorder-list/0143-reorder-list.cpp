/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        // Return early if provided head is empty
        if (head == nullptr) {
            return;
        }

        // Create an empty container to store ListNode*
        // and attach head to curr
        vector<ListNode*> nodes;
        ListNode* curr = head;

        // Push every nodes into container by going through the linkedlist
        while (curr != nullptr) {
            nodes.push_back(curr);
            curr = curr->next;
        }

        int L = 0;
        int R = static_cast<int>(nodes.size()) - 1;

        // Reorder nodes using left/right pointers
        while (L < R) {
            nodes[L]->next = nodes[R];
            L++;
            nodes[R]->next = nodes[L];
            R--;
        }
        // Set the tail's next pointer points to prevent a cycle
        nodes[L]->next = nullptr;
    }
};