from typing import List


class Solution:
    def findPeakElement_BF(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if (i == 0 or nums[i] > nums[i-1]) and (i == n-1 or nums[i]>nums[i+1]):
                return i
        return -1

    def findPeakElement_Optimized(self, nums: List[int]) -> int:
        """
        using Binary search, algo
        think of putting the values in a graph(curves)
        and then try to think of the peaks
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[n-1] > nums[n-2]: return n-1
        low = 1
        high = n-2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid -1 ] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.findPeakElement_BF(nums = [1,2,5,1,2,1]))
    print(sol.findPeakElement_Optimized(nums = [1,2,5,1,2,1]))