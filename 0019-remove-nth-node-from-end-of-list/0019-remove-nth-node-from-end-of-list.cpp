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
        // Create an empty container to store ListNode*
        // and attach head to curr
        vector<ListNode*> nodes;
        ListNode* curr = head;

        // Push every nodes into container by going through the linkedlist
        while (curr != nullptr) {
            nodes.push_back(curr);
            curr = curr->next;
        }

        const int removeIdx = static_cast<int>(nodes.size()) - n;

        // Return early without doing the removal
        if (removeIdx == 0) {
            return head->next;
        }

        // Remove the target node from the linkedlist
        nodes[removeIdx - 1]->next = nodes[removeIdx]->next;

        // Return the modified linkedlist's head
        return head;
    }
};