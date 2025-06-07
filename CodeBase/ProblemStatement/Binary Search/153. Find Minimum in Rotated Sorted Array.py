from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = float('inf')
        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[high]:
                if nums[low] < ans:
                    ans = nums[low]
                break
            if nums[low] <= nums[mid]:
                if ans >=nums[low]:
                    ans = nums[low]
                low = mid + 1
            else:
                if ans >= nums[mid]:
                    ans = nums[mid]
                high = mid - 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMin(nums = [3,4,5,6,7,0,1,2]))