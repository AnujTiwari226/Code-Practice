class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        if not s:
            return s
        res = ''
        balance = 0
        start = 0
        for i in range(len(s)):
            if s[i] == '(':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                start += 1
                res += s[start:i]
                start = i+1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeOuterParentheses("()"))