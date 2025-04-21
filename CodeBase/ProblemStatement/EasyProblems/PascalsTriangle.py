class Solution:

    def get_ele_at_row_col(self, row, col):
        """
        we will get the ele from give row and col
        we are using nCr formula
            nCr = n! // r! * (n - r)!
        so first we convert the row and col to index based num i.e. row - 1 and col - 1
        then we try to observer one pattern in nCr formula -
            the numerator factorial will run only c times meaning for row = 6 and col = 3
            n = row - 1 = 5 and r = col - 1 = 2
            then nCr value will be equals to (5*4) // (2*1)
                2 values in numerator and 2 in denominator which is same as r i.e. col - 1
        :param row:
        :param col:
        :return:
        Time complexity will be O(r)
        """
        res = 1
        n = row - 1
        r = col - 1
        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)
        return res


    def get_the_nth_row(self, nrow):
        """
        we will get the entire nth row of Pascal's Triangle
        we are using the get_ele_at_row_col method to get each element in the row
        for a given row number nrow, we iterate through each column position (1 to nrow)
        and get the element at that position using get_ele_at_row_col
        :param nrow: the row number to retrieve (1-based index)
        :return: list of lists containing the elements of the nth row
                 returns [[]] for nrow == 0 as special case
        time complexity for this approach is O(n * r) where n for the iteration and r from the method to get ele
            from given row and col
        """
        if nrow == 0:
            return [[]]
        ans = []
        for i in range(1, nrow+1):
            ans.append([self.get_ele_at_row_col(nrow, i)])
        return ans

    def get_the_nth_row_in_optimal_way(self, nrow):
        """
        we will get the entire nth row of Pascal's Triangle in optimal way without using nested loop
        this approach uses the property that each element in row n can be derived from the previous element:
            current_element = previous_element * (nrow - current_position) // current_position
        we start with 1 as the first element, then iteratively calculate each subsequent element
        :param nrow: the row number to retrieve (1-based index)
        :return: list of lists containing the elements of the nth row
                 returns [[]] for nrow == 0 as special case
        Time Complexity = O(n)
        """
        if nrow == 0:
            return [[]]
        ans = 1
        res = [[ans]]
        for i in range(1, nrow):
            ans = ans * ( nrow - i)
            ans = ans // i
            res.append([ans])
        return res

    def get_pascal_triangle(self, n):
        """
        Generates Pascal's Triangle up to the nth row (0-based index)
        Each element is calculated using the get_ele_at_row_col method which applies the nCr formula:
            nCr = n! / (r! * (n - r)!)
        The triangle is constructed by:
            1. Iterating through each row from 1 to n
            2. For each row, calculating all column values using combinatorial logic
            3. Appending each completed row to the result
        Note: Returns [[]] for n == 0 as special case
        :param n: The number of rows to generate (0-based)
        :return: List of lists representing Pascal's Triangle
                 Each sublist represents a row, e.g., for n=2: [[1], [1,1], [1,2,1]]
        """
        if n == 0:
            return [[]]
        ans = []
        for row in range(1, n+1):
            temp = []
            for col in range(1, row+1):
                temp.append(self.get_ele_at_row_col(row, col))
            ans.append(temp)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # 1. get ele at rth row and cth col
    print(sol.get_ele_at_row_col(6, 3))
    # 2. get the entire row for n
    print(sol.get_the_nth_row(6))
    # 2.II . get the entire row for n but in optimal way
    print(sol.get_the_nth_row_in_optimal_way(6))
    # 3. print the entire pascal triangle till n
    print(sol.get_pascal_triangle(6))
