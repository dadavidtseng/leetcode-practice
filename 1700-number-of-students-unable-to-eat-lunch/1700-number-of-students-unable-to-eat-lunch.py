class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        q = deque(students)
        idx = 0

        while q and idx < len(sandwiches):
            if not sandwiches[idx] in q:
                break
            if q[0] == sandwiches[idx]:
                q.popleft()
                idx += 1
            else:
                q.append(q.popleft())
        return len(q)
