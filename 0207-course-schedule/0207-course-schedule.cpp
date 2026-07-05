class Solution {
   public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // Create adjacency list
        // Create the state for every nodes
        // 0=unvisited, 1=in-progress, 2=done
        vector<vector<int>> node(numCourses);
        vector state(numCourses, 0);

        // Iterate through prerequisites to build the graph
        // node(course -> prereq)
        for (int i = 0; i < static_cast<int>(prerequisites.size()); ++i) {
            int const course = prerequisites[i][0];
            int const prereq = prerequisites[i][1];

            node[course].push_back(prereq);
        }

        // Iterate through every courses,
        // return false if any cycle is found
        // Note that we're using numCourses here instead of prerequisites
        // because the prerequisites.size() might be greater or equal than numCourses
        for (int i = 0; i < numCourses; ++i) {
            if (dfs(node, state, i)) {
                return false;
            }
        }

        // Return true if no cycle was found
        return true;
    }

    //------------------------------------------------------------------------------------------------
    bool dfs(vector<vector<int>> const& node, vector<int>& state, int i) {
        // Return true if this node is still in-progress,
        // means that we've found a cycle
        if (state[i] == 1) {
            return true;
        }

        // Return false if this node is done,
        // means that we're safe to take it
        if (state[i] == 2) {
            return false;
        }

        // Mark this node's state as in-progress since it's unvisited
        state[i] = 1;

        // Iterate through this course(node)'s every prerequisites(neighbor nodes)
        // return true if any cycle was found
        for (int j = 0; j < static_cast<int>(node[i].size()); ++j) {
            int neighbor = node[i][j];

            if (dfs(node, state, neighbor)) {
                return true;
            }
        }

        // Mark this course(node)'s state as completed since we didn't find any cycle
        state[i] = 2;

        return false;
    }
};
