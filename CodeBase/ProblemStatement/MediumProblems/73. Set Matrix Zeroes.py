from typing import List


class Solution:
    def setZeroes_BF(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        This solution modifies the input matrix in-place to set entire rows and columns
        to zero if any element is zero.

        Approach:
        1. First pass:
           - Traverse the matrix to find elements with value 0.
           - For each 0 found at (i, j), mark all non-zero elements in its row and column as -1.
             This acts as a temporary marker to avoid modifying the matrix prematurely.
        2. Second pass:
           - Traverse the matrix again and convert all -1 values to 0.

        Notes:
        - This approach avoids using extra space (O(1) space complexity).
        - It assumes that -1 is not a valid value in the original matrix.
          If -1 can exist as a legitimate value, this approach may give incorrect results.

        Time Complexity: O((n × m) * (n + m) + (n * m)) ~= n**3
        Space Complexity: O(1)
        """
        n, m = len(matrix), len(matrix[0])

        # cols = [0] * m -> matrix[0][..]
        # rows = [0] * n -> matrix[..][0]
        def markrow(i):
            for j in range(m):
                if matrix[i][j] != 0:
                    matrix[i][j] = float('-inf')

        def markcol(j):
            for i in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float('-inf')

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    markrow(i)
                    markcol(j)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == float('-inf'):
                    matrix[i][j] = 0

    def setZeroes_optimal(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Modifies the given matrix in-place such that if an element is 0, its entire row and column are set to 0.

        Approach:
        1. Use two auxiliary arrays:
           - `rows` of size n (number of rows)
           - `cols` of size m (number of columns)
        2. First pass:
           - Traverse the matrix and mark which rows and columns need to be zeroed
             by setting rows[i] = 1 and cols[j] = 1 when matrix[i][j] == 0.
        3. Second pass:
           - Traverse the matrix again and set matrix[i][j] = 0
             if rows[i] == 1 or cols[j] == 1.

        This method uses O(n + m) extra space for tracking zero-affected rows and columns.

        Time Complexity: O((n × m) + (n * m))
        Space Complexity: O(n + m)
        """
        n, m = len(matrix), len(matrix[0])

        cols = [0] * m
        rows = [0] * n
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    cols[j] = 1
                    rows[i] = 1
        for i in range(n):
            for j in range(m):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0






if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes_BF(matrix)
    print('Brute Force approach - ', matrix)
    print('matrix 2')
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes_optimal(matrix1)
    print('Optimal approach - ', matrix1)
