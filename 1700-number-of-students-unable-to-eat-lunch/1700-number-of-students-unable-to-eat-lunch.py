class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        result = len(students)
        freq = {}

        for s in students:
            freq[s] = freq.get(s, 0) + 1

        for s in sandwiches:
            if freq.get(s, 0) > 0:
                result -= 1
                freq[s] -= 1
            else:
                break
        return result
