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
        // Return early if provided head is empty or there's only one node in
        // the linkedlist
        if (head == nullptr || head->next == nullptr) {
            return;
        }
        auto dfs = [&](this auto&& self, ListNode*& front,
                       ListNode* back) -> bool {
            // Return true if back is empty
            if (back == nullptr) {
                return true;
            }

            if (!self(front, back->next)) {
                // Note that this could return whatever because it's just for
                // existing the DFS call
                return false;
            }

            // Set the new tail (back->next) to empty and return false
            if (front == back || front->next == back) {
                back->next = nullptr;
                return false;
            }

            // Reorder nodes using front/back pointers
            ListNode* temp = front->next;
            front->next = back;
            back->next = temp;
            front = temp;

            return true;
        };
        dfs(head, head->next);
    }
};