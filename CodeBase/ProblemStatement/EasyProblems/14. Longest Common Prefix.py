from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        res = ''
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i]!=char:
                    return strs[0][:i]
        return strs[0]




if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(strs = ["flower","flow","flight"]))
