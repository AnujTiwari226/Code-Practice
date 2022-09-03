from typing import List


class Solution:
    def getLongestPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s1, s2 = strs[0], strs[-1]
        for i, ch in enumerate(s1):
            if ch != s2[i]:
                return s1[:i]


print(Solution().getLongestPrefix(['flower', 'flight', 'flow']))
