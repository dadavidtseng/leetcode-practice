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
        // Find the middle node in linkedlist using slow/fast pointers
        ListNode* slow = head;
        ListNode* fast = head;

        // Advance slow/fast pointers when
        // 1. Fast pointer is not nullptr(even list)
        // 2. Fast pointer's next is not nullptr(odd list)
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Split the list in half
        // 1. Attach original head to first
        // 2. Attach slow pointer's next to second(this works both on odd/even
        // list)
        // 3. Cut the second half from first half(original head)
        ListNode* first = head;
        ListNode* second = slow->next;
        slow->next = nullptr;

        // Reverse the second list
        // 1. Store the next node in temp
        // 2. Set the next node to prev
        // 3. Advance the prev node
        // 4. Advance the curr node
        // Attach prev to the head of second half(cur is nullptr now)
        ListNode* prev = nullptr;
        ListNode* curr = second;

        while (curr != nullptr) {
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        second = prev;

        // Iterate through the first haft and insert the second half one after
        // another in first half exit the loop when second is empty
        //
        // Note that we don't need to check first because for first half is one
        // node more than second half in odd list
        while (second != nullptr) {
            ListNode* tempFirst = first->next;
            ListNode* tempSecond = second->next;

            // Reorder nodes
            first->next = second;
            second->next = tempFirst;

            // Advance first and second for next iteration
            first = tempFirst;
            second = tempSecond;
        }
    }
};