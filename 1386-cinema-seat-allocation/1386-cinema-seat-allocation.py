"""
Understand:
Provided a nested integer array reservedSeats and n * 10 matrix
Return the maximum number of groups that can be assigned
Rules:
1. We can only assign group to [2,3,4,5], [4,5,6,7], [6,7,8,9]
2. A seat can only be assigned once
3. When the seat is in reservedSeats, we can't assign it

In example 1, notice that if seat 2-9 are all unreserved, in order to assign optimally,
we'd want to assign [2,3,4,5] and [6,7,8,9] instead of [4,5,6,7].

Match:
Intervals, Matrix, Greedy?

Plan:
Iterate through this 2D matrix, when [2,5] is assignable, we can jump to check [6,9];
when [2,5] isn't assignable, we need to check [4,7]. Basically, once an interval is assignable,
we need to jump to the one after.
"""


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        result = 0
        row_to_seat = {}
        for row, col in reservedSeats:
            if row not in row_to_seat:
                row_to_seat[row] = set()
            row_to_seat[row].add(col)

        for reserved in row_to_seat.values():
            can_first = all(seat not in reserved for seat in [2, 3, 4, 5])
            can_mid = all(seat not in reserved for seat in [4, 5, 6, 7])
            can_last = all(seat not in reserved for seat in [6, 7, 8, 9])

            if can_first and can_last:
                result += 2
            elif can_first or can_mid or can_last:
                result += 1
        return result + 2 * (n - len(row_to_seat))


"""
Review
It turned out that we didn't need a matrix, but we need to transform reservedSeats into a queryable row_to_seat so that we can visit a row and ask for seats to see if it's assignable.
I was able to get can_first, can_mid, can_last, but I guess next time I shouldn't assume that
we should always use 2D matrix when seeing that kind of diagram.

Evaluate
I prefer this `reservedSeats -> row_to_seat` solution because it's easier to read, comparing to bitwise solution. However, a bitwise solution is something worth trying and knowing as well.

Complexity
Time: O(m)
Space: O(m)
Where m is the length of reservedSeats
"""
