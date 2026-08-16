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
        auto conquer = [](ListNode* listA, ListNode* listB) -> ListNode* {
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
        auto divide = [&](this auto&& self, vector<ListNode*>& lists, int L,
                          int R) -> ListNode* {
            // Return empty if left/right pointers cross
            if (L > R) {
                return nullptr;
            }
            // Return lists[L] if this is lists has an odd size
            if (L == R) {
                return lists[L];
            }

            // Calculate mid pointer for divide
            const int M = L + (R - L) / 2;

            // Recursively call divide function until there are one left and one
            // right
            ListNode* left = self(lists, L, M);
            ListNode* right = self(lists, M + 1, R);

            // Conquer left/right ListNode when unwinding
            return conquer(left, right);
        };

        // Return nullptr if lists is empty
        if (lists.empty()) {
            return nullptr;
        }

        // Return divid and conquer using left/right pointers start from the
        // first and last idx
        return divide(lists, 0, static_cast<int>(lists.size()) - 1);
    }
};