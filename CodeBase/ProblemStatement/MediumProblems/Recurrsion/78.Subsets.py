from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def helper(idx, temp):
            if idx >= n:
                res.append(temp[:])
                return
            temp.append(nums[idx])
            #take condition
            helper(idx+1, temp)
            temp.remove(nums[idx])
            #not take condition
            helper(idx+1, temp)
        helper(0, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.subsets(nums))