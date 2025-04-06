from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        brd = [['.' for _ in range(n)] for _ in range(n)]

        def safe(r, c):
            row = r
            col = c
            #upper diagonal check
            while row >= 0 and col >= 0:
                if brd[row][col] == 'Q': return False
                row -= 1
                col -= 1
            # left row check
            row, col = r, c
            while col >= 0:
                if brd[row][col] == 'Q': return False
                col -= 1
            # lower diagonal check
            row, col = r, c
            while row < n and col >= 0:
                if brd[row][col] == 'Q': return False
                row += 1
                col -= 1
            return True


        def place(col):

            if col == n:
                res.append([''.join(row) for row in brd])
                return
            for row in range(n):
                if safe(row, col):
                    brd[row][col] = 'Q'
                    place(col+1)
                    brd[row][col] = '.'
        place(0)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.solveNQueens(4))