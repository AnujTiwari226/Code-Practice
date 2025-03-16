from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n , m = len(matrix), len(matrix[0])
        cols = [0] * m
        rows = [0] * n
        for i in range (n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
        for i in range(n):
            for j in range(m):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
        return matrix


    def setZeros(self, matrix: List[List[int]]) -> None:

        n , m = len(matrix), len(matrix[0])
        # cols = [0] * m -> matrix[0][..]
        # rows = [0] * n -> matrix[..][0]
        col0 = 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # mark ith row
                    matrix[i][0] = 0
                    # mark jth cols
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0

        return matrix

