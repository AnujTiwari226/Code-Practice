from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        right -> bottom -> left -> top : this approach recursively gives us spiral
        """
        n = len(matrix)
        m = len(matrix[0])
        left, top = 0, 0
        bottom, right = n - 1, m - 1
        res = []
        print(f'left = {left}, top = {top}, right = {right}, bottom = {bottom}')
        while top <= bottom and left <= right:

            # right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # left
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res


if __name__ == '__main__':
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.spiralOrder(matrix))
    print('matrix 2')
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(sol.spiralOrder(matrix1))
