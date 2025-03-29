class Solution:
    def generateParenthesis(self, n):
        def helper(current, open, close, res):
            if current == 2*n:
                res.append(current)
            print(f'Current before open and close if - {[current]}')
            if open < n:
                helper(current + '(', open+1, close, res)
                print(f'Current after open if - {[current]}')
            if close < open:
                helper(current+')', open, close+1, res)
                print(f'Current after close if - {[current]}')
        res = []
        helper("", 0, 0, res)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(3))