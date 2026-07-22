/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        // Exit the while loop if we are
        // 1. At the end of the linked list
        // 2. At one node before the end of the linked list
        while (fast != nullptr && fast->next != nullptr) {
            // Advance slow pointer by one node
            // and fast pointer by two nodes
            slow = slow->next;
            fast = fast->next->next;

            // Return true if slow equals to fast
            if (slow == fast) {
                return true;
            }
        }
        // Return false if we've reached the end of the linked list
        return false;
    }
};