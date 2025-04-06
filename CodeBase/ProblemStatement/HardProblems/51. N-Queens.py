from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        brd = [['.' for _ in range(n)] for _ in range(n)]
        leftrow = [0] * n
        upper = [0] * ((2 * n) - 1)
        lower = [0] * ((2 * n) - 1)

        def solve(col, leftrow, upper, lower):

            if col == n:
                res.append([''.join(row) for row in brd])
                return
            for row in range(n):
                if (leftrow[row] == 0) and (upper[row + col] == 0) and (lower[(n - 1) + (col - row)]) == 0:
                    brd[row][col] = 'Q'
                    leftrow[row] = 1
                    upper[row + col] = 1
                    lower[(n - 1) + (col - row)] = 1
                    solve(col + 1, leftrow, upper, lower)
                    brd[row][col] = '.'
                    leftrow[row] = 0
                    upper[row + col] = 0
                    lower[(n - 1) + (col - row)] = 0

        solve(0, leftrow, upper, lower)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.solveNQueens(4))