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
        auto mergeTwoLists = [](ListNode* listA, ListNode* listB) -> ListNode* {
            // Create a dummy node that points to nothing
            // and attach a tail node on that dummy node
            ListNode dummy(0, nullptr);
            ListNode* tail = &dummy;

            // Exit the while loop when listA and listB are both exhausted
            while (listA != nullptr && listB != nullptr) {
                // If listA's value is smaller than listB's value
                // 1. Attach listA to tail
                // 2. Advance listA
                if (listA->val < listB->val) {
                    tail->next = listA;
                    listA = listA->next;
                }
                // If listA's value is larger or equal to listB's value
                // 1. Attach listB to tail
                // 2. Advance listB
                else {
                    tail->next = listB;
                    listB = listB->next;
                }

                // Advance tail
                tail = tail->next;
            }

            // Attach the remaining of listA and listB to tail
            tail->next = (listA != nullptr) ? listA : listB;

            // Return the head of the merged list
            return dummy.next;
        };

        // Return nullptr if lists is empty
        if (lists.empty()) {
            return nullptr;
        }

        // Iterate through lists from index 1 and merge them one by one
        for (int i = 1; i < static_cast<int>(lists.size()); ++i) {
            lists[i] = mergeTwoLists(lists[i], lists[i - 1]);
        }
        return lists.back();
    }
};