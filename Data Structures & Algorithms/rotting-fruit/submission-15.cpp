class Solution {
   public:

   int freshCount = 0;
   int time = 0;

    void spread(int rows, int cols, deque<tuple<int, int, int>>& rotten, vector<vector<int>>& grid) {
        auto [r, c, t] = rotten.front();
        rotten.pop_front();

        time = t > time ? t : time;

        for (auto d : {-1, 1}) {
            for (auto [nr, nc] : std::array{
                std::pair{r + d, c},
                std::pair{r, c + d}
            }) {
                if (nr < 0 || nr >= rows ||
                    nc < 0 || nc >= cols ||
                    grid[nr][nc] != 1) {
                    continue;
                }
                grid[nr][nc] = 2;
                rotten.push_back({nr, nc, t + 1});
                freshCount--;
            }
        }
    }

    int orangesRotting(vector<vector<int>>& grid) {
        deque<tuple<int, int, int>> rotten;
        int rows = grid.size();
        int cols = grid[0].size();

        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) {
                    rotten.push_back({r, c, 0});
                }
                if (grid[r][c] == 1) {
                    freshCount++;
                }
            }
        }

        while (!rotten.empty()) {
            spread(rows, cols, rotten, grid);
        }

        return freshCount == 0 ? time : -1;
    }
};
