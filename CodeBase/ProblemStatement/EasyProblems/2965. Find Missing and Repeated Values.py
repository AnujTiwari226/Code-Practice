from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        Finds the repeated and missing values in an n x n grid where each number from 1 to n^2 appears exactly once,
        except for one repeated number and one missing number.

        The method uses mathematical properties to efficiently determine the repeated and missing values by comparing
        the actual sum and sum of squares of the grid elements with their expected values.

        Args:
            grid (List[List[int]]): A 2D list representing the n x n grid of integers.

        Returns:
            List[int]: A list containing two integers: the repeated value followed by the missing value.

        Approach:
            1. Flatten the 2D grid into a 1D list for easier processing.
            2. Calculate the actual sum of the elements and compare it with the expected sum of numbers from 1 to n^2.
               The difference gives the equation: repeated - missing = actual_sum - expected_sum.
            3. Calculate the actual sum of the squares of the elements and compare it with the expected sum of squares
               of numbers from 1 to n^2. The difference gives another equation involving both the repeated and missing numbers.
            4. Solve the system of equations derived from the sum and sum of squares differences to find the repeated and missing values.
        """
        temp = []
        for ele in grid:
            temp.extend(ele)
        n = len(temp)
        actual = sum(temp)
        exp = n * (n+1) // 2
        s = actual - exp # repeated - missing

        sq_s = sum(x * x for x in temp)
        exp_sq_s = n * (n+1) * (2*n+1) // 6
        s2 = sq_s - exp_sq_s # repeated^2 * missing ^2 = (repeated-missing)(repeated+missing) here (repeated-missing) = s
        #repeated+missing = s2 // s
        r_plus_m = s2 // s

        # solve s = repeated - missing and repeated+missing = s2 // s first add then subtract
        repeated = ((s2 // s) + s) // 2
        missing = ((s2 // s) - s) // 2
        return [repeated, missing]

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMissingAndRepeatedValues(grid = [[1, 2, 3], [2, 4, 5], [6, 7, 8]]))