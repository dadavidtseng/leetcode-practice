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
        int nodesSize = 0;
        ListNode* curr = head;

        // Calculate the number of nodes in the linkedlist by iterating through
        // it
        while (curr != nullptr) {
            nodesSize++;
            curr = curr->next;
        }

        const int removeIdx = nodesSize - n;

        // Return early without doing the removal
        if (removeIdx == 0) {
            return head->next;
        }

        // Move current node back to head for next iteration
        curr = head;

        // Iterate through the linkedlist again and break after removing the
        // target node
        for (int i = 0; i < nodesSize; ++i) {
            if ((i + 1) == removeIdx) {
                curr->next = curr->next->next;
                break;
            }
            curr = curr->next;
        }

        // Return the modified linkedlist's head
        return head;
    }
};