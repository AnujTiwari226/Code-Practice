from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = 0
        curr = 0
        for num in nums:
            curr += num
            if curr < min_sum:
                min_sum = curr
        start_value = 1 - min_sum
        return  max(1, start_value)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minStartValue(nums = [-3,2,-3,4,2]))