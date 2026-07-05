class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        q = deque()

        for course in range(numCourses):
            if in_degree[course] == 0:
                q.append(course)

        result = []

        while q:
            prereq = q.popleft()

            result.append(prereq)

            for course in graph[prereq]:
                in_degree[course] -= 1

                if in_degree[course] == 0:
                    q.append(course)

        return result if len(result) == numCourses else []
