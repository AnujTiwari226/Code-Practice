from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        total = 0
        max_freq = 0
        for r in range(len(nums)):
            # ele = nums[r]
            total += nums[r]
            # window_size = (r-l+1)
            while (r-l+1)*nums[r] - total > k:
                # passed_condition = (r - l + 1)*nums[r]
                total -= nums[l]
                l += 1
            # failed_condition = (r - l + 1)*nums[r]
            max_freq = max(max_freq, r-l+1)
        return max_freq


if __name__ == '__main__':
    sol = Solution()
    sol.maxFrequency([1,4,8,13], 5)