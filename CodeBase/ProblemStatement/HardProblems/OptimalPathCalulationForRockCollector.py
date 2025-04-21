class Solution:
    def optimalPath(self, grid):
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        # grid = [
        #     [550, 0, 0, 0, 5],
        #     [5, 1, 1, 1, 0],
        #     [2, 0, 0, 0, 200]
        # ]
        for row in range(rows-1, -1, -1):
            for col in range(cols):
                curr = grid[row][col]

                north = dp[row+1][col] if row+1 < rows else 0
                east = dp[row][col-1] if col-1 >= 0 else 0

                dp[row][col] = curr + max(north, east)\

        return dp[0][cols-1]


if __name__ == '__main__':
    sol = Solution()
    grid = [
    [550, 0,   0,   0,   5],
    [5,   1,   1,   1,   0],
    [2,   0,   0,   0, 200]
]
    print(sol.optimalPath(grid))