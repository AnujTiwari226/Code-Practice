from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        def helper(idx, curr):
            if idx == len(digits):
                res.append("".join(curr))
                return

            digit = digits[idx]
            for char in digit_map[digit]:
                curr.append(char)
                helper(idx+1, curr)
                curr.pop()
        helper(0, [])
        return res41

if __name__ == '__main__':
    sol = Solution()
    test_cases = ['23', '2', '', '34']
    for d in test_cases:
        print(sol.letterCombinations(d))