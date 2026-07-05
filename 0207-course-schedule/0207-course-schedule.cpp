class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> node(numCourses);
        vector<int> inDegree(numCourses, 0);

        for (int i = 0; i < static_cast<int>(prerequisites.size()); ++i) {
            int const course = prerequisites[i][0];
            int const prereq = prerequisites[i][1];

            node[prereq].push_back(course);
            inDegree[course]++;
        }

        queue<int> q;

        for (int i = 0; i < numCourses; ++i) {
            if (inDegree[i] == 0) {
                q.push(i);
            }
        }

        int count = 0;

        while (!q.empty()) {
            const int i = q.front();
            q.pop();

            count += 1;

            for (int j = 0; j < (int)node[i].size(); ++j) {
                int neighbor = node[i][j];
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        return count == numCourses;
    }
};