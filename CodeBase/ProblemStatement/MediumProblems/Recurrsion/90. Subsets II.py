from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def helper(idx, ds):
            res.append(ds.copy())
            for i in range(idx, n):
                if i != idx and nums[i] == nums[i-1]:
                    continue
                ds.append(nums[i])
                helper(i+1, ds)
                ds.pop()
        helper(0 , [])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsetsWithDup(nums = [1,2,2]))