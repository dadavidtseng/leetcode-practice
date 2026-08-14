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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        auto dfs = [&](this auto&& self, ListNode* head, int& n) -> ListNode* {
            // Return empty if we've reached the end of the linkedlist
            if (head == nullptr) {
                return nullptr;
            }

            // The shape of the DFS call is
            // DFS(head){head's next}, so it's iterating through the linkedlist
            head->next = self(head->next, n);

            // n was passed in by reference in order to really modify it in DFS
            // call
            n--;

            // Return this node's next node so that it can be linked with this
            // node's previous node, which is essentially removing this node
            // from the linked list
            if (n == 0) {
                return head->next;
            }

            // Return head, which was passed in this DFS call
            // so that the unwinding process won't modify anything in the
            // linkedlist
            return head;
        };
        return dfs(head, n);
    }
};