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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;

        while (true) {
            // minIdx for picking out the list with smallest node value
            // Note that -1 means nothing has been picked yet
            int minIdx = -1;

            // Iterate through lists
            for (int i = 0; i < static_cast<int>(lists.size()); ++i) {
                // Continue if lists[i] is empty
                if (lists[i] == nullptr) {
                    continue;
                }

                // If we haven't picked anything or
                // if current node's value is smaller than what node we've
                // picked's value, set minIdx to current idx, which means
                // picking that node
                if (minIdx == -1 || lists[i]->val < lists[minIdx]->val) {
                    minIdx = i;
                }
            }

            // Break out of the while loop if we have nothing to pick
            if (minIdx == -1) {
                break;
            }

            // 1. Attach the picked node to current node
            // 2. Advance the list that has been picked for next iteration
            // 3. Advance current node
            curr->next = lists[minIdx];
            lists[minIdx] = lists[minIdx]->next;
            curr = curr->next;
        }
        return dummy->next;
    }
};