class Solution:
    def findKRotation(self, nums):
        low = 0
        high = len(nums) - 1
        ans = float('inf')
        idx = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[high]:
                if nums[low] < ans:
                    ans = nums[low]
                    idx = low
                break
            if nums[low] <= nums[mid]:
                if ans >= nums[low]:
                    ans = nums[low]
                    idx = low
                low = mid + 1
            else:
                if ans > nums[mid]:
                    ans = nums[mid]
                    idx = mid
                high = mid - 1
        return idx


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKRotation(nums = [3,4,5,6,7,0,1,2]))