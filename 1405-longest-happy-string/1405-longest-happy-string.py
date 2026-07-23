"""
Given integers a, b, and c, which represent the most occurrences of letter a, b, and c.
Return any of the longest happy string.

A happy string is,
1. Contains a, b, or c
2. Doesn't contain aaa, bbb, ccc as substring
3. Contains at most a/b/c occurrences for letter a/b/c

0 <= a, b, c <= 100
a + b + c > 0

Match:
String, Backtracking?, Stack?

Plan:
Substring aaa/bbb/ccc is the biggest constrain
Maybe we could use a stack and check if stack[-1] and stack[-2] both are the same letter,
when that happen, we pick another one if available. But would that always be the "longest"?
Maybe we should pick the largest number among a/b/c?

a=0, b=1, c=5
[c,b,a]
1. c
2. cc, we can't pick c for next round
3. ccb
4. ccbc
5. ccbcc
"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        store = [a, b, c]
        result = []

        def get_max_idx(repeated_idx: int) -> int:
            # Initialize max_idx and max_count
            max_idx = -1
            max_count = 0

            # Iterate through everything in store
            for i in range(3):
                # Continue if we hit the repeated_idx or this index is 0
                if i == repeated_idx or store[i] == 0:
                    continue
                # Record the max_count using store[i]
                # and assign i to max_idx
                if max_count < store[i]:
                    max_count = store[i]
                    max_idx = i
            # Return max_idx after the for loop above,
            # max_idx will equal -1 if we didn't find anything
            return max_idx

        repeated_idx = -1
        while True:
            max_idx = get_max_idx(repeated_idx)

            # Break for return if we didn't find anything in get_max_idx function,
            # which means that we have nothing else to find
            if max_idx == -1:
                break

            # Push the character into result
            # and decrement the letter count in store by 1
            # Note that max_idx is 0/1/2 for letter a/b/c
            # so that we do max_idx + ord("a") and then chr()
            result.append(chr(max_idx + ord("a")))
            store[max_idx] -= 1

            # Assign max_idx to repeated_idx to avoid using the same letter for the third time
            if len(result) >= 2 and result[-1] == result[-2]:
                repeated_idx = max_idx
            else:
                repeated_idx = -1
        return "".join(result)


"""
Review:
First time doing medium question without using any ai, the intuitive I got was actually correct.
I came up with a greedy solution, it was the implementation part I got stuck there.

Always pick the most remaining letter will get us the highest chance for longest happy string.

Evaluate:
Next time I should write comments or pseudocode in implementation before writing any codes.
Also, don't forget to consider a helper function for better readibility.
"""
