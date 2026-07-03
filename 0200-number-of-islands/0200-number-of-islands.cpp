class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int result = 0;
        const int rowSize = static_cast<int>(grid.size());
        const int colSize = static_cast<int>(grid[0].size());

        // Iterate through every grid
        for (int row = 0; row < rowSize; ++row) {
            for (int col = 0; col < colSize; ++col) {
                // Only enter the bfs call if that grid is "1",
                // which means that it is part of the island;
                // Increment the result by 1 after the bfs call,
                // which means that we've found an island
                if (grid[row][col] == '1') {
                    bfs(grid, row, col);
                    result++;
                }
            }
        }
        return result;
    }

    void bfs(vector<vector<char>>& grid, int row, int col) {
        const int rowSize = static_cast<int>(grid.size());
        const int colSize = static_cast<int>(grid[0].size());

        // Push this grid's row/col index in the queue
        // and mark this grid as visited
        queue<pair<int, int>> q;
        q.push(pair<int, int>(row, col));
        grid[row][col] = '0';

        // Exit the while loop when there's nothing to process
        // Note that "while (!q.empty())" is short for "while (q.size() != 0)"
        while (!q.empty()) {
            auto [qRow, qCol] = q.front();
            q.pop();

            static constexpr pair<int, int> directions[] = {
                {-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // up, down, left, right

            // Spread the bfs call in four directions
            for (auto const& [r, c] : directions) {
                int nextRow = qRow + r;
                int nextCol = qCol + c;

                // Continue if next grid is out of bound
                if (nextRow < 0 || nextCol < 0 || nextRow >= rowSize ||
                    nextCol >= colSize) {
                    continue;
                }

                // Continue if next grid has already been visited so that we
                // don't count it again
                if (grid[nextRow][nextCol] == '0') {
                    continue;
                }

                // Mark this grid as visited
                grid[nextRow][nextCol] = '0';

                // Push next grid's row/col index in the queue
                q.push(pair<int, int>(nextRow, nextCol));
            }
        }
    }
};
