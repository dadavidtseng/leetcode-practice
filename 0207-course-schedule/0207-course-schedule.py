class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node: List[List[int]] = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            node[prereq].append(course)
            in_degree[course] += 1

        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        count = 0
        while q:
            i = q.popleft()
            count += 1

            for neighbor in node[i]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return count == numCourses
