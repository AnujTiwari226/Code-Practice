from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(idx, rem_target, curr):
            if rem_target == 0:
                res.append(curr.copy())
                return
            for i in range(idx, len(candidates)):
                ele = candidates[i]
                if ele > rem_target:
                    break
                if i > idx and ele == candidates[i-1]:
                    continue
                curr.append(ele)
                helper(i+1, rem_target-ele, curr)
                curr.pop()
        helper(0, target, [])
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))