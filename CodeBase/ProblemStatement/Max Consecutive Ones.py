from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        templ, maxl, i = 0, 0, 0
        while i < len(nums):
            if nums[i] == 1:
                templ += 1
            else:
                maxl = max(maxl, templ)
                templ = 0
            i += 1
        return max(maxl, templ)


if __name__  == '__main__':
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))