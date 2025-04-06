from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= []
        n= len(nums)
        freq = [0]*n
        def helper(ds, freq):
            if len(ds) == n:
                res.append(ds[:])
                return
            for i in range(n):
                if not freq[i]:
                    freq[i] = 1
                    ds.append(nums[i])
                    helper(ds, freq)
                    ds.pop()
                    freq[i] = 0
        helper([], freq)
        return res

    def permute_Approach_II(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def helper(idx, ds):
            if idx == n:
                ds = []
                for i in range(n):
                    ds.append(nums[i])
                res.append(ds.copy())
                return
            for i in range(idx, n):
                nums[i], nums[idx] = nums[idx], nums[i]
                helper(idx+1, ds)
                nums[i], nums[idx] = nums[idx], nums[i]

        helper(0, [])
        return res
if __name__ == '__main__':
    sol = Solution()
    print(sol.permute_Approach_II(nums = [1,2,3]))
