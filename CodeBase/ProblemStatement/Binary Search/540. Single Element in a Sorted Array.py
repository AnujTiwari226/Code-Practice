from typing import List


class Solution:
    def singleNonDuplicate_BF(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        for i in range(n):
            if i == 0 and nums[i] != nums[i+1]:
                return nums[i]
            elif i == n-1  and nums[i] != nums[n-2]:
                return nums[i]
            else:
                if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                    return nums[i]
        return -1

    def singleNonDuplicate_Optimized(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if nums[0] != nums[1]: return nums[0]
        if nums[n-1] != nums[n-2]: return nums[n-1]
        low = 1
        high = n-2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            elif ((mid % 2 == 1 and nums[mid-1] == nums[mid])
                  or (mid % 2 == 0 and nums[mid+1] == nums[mid])) :
                low = mid + 1
            else:
                high = mid - 1

        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNonDuplicate_BF(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]))
    print(sol.singleNonDuplicate_Optimized(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]))