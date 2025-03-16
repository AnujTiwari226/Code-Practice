from typing import List
from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums):
        slow = 2
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0 : return
        end_idx = len(nums1) - 1
        while n > 0 and m > 0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[end_idx] = nums2[n-1]
                n -= 1
            else:
                nums1[end_idx]  = nums1[m-1]
                m -= 1
            end_idx -= 1
        while n > 0:
            nums1[end_idx] = nums2[n-1]
            n -= 1
            end_idx -= 1
        return nums1

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        n = len(nums) - 1
        for i in range(n):
            ele = nums[i]
            if ele == 0:
                return False
            if ele + i >= n:
                return True
            while ele > 0:
                val = i + nums[ele]
                subele = nums[i + nums[ele]]
                if subele + ele + i - n >= 0 and subele != 0:
                    return True
                ele -= 1
        return False

    def canJump_method2(self, nums):
        mysum = 0
        for n in nums:
            if mysum < 0:
                return False
            elif n > mysum:
                mysum = n
            mysum -= 1
        return True

    def maxProfit(self, prices: List[int]) -> int: # 122. Best Time to Buy and Sell Stock II (dp method)
        n = len(prices)
        dp = {}
        profit = self.get_profit(i=0, buy=1, arr = prices, n=n, dp=dp)
        return profit

    def get_profit(self, i, buy, arr, n, dp):
        if i == n: return 0
        profit = 0
        if (i, buy) in dp:
            return dp[(i, buy)]
        if buy:
            profit = max(-arr[i] + self.get_profit(i+1, 0, arr, n, dp), 0 + self.get_profit(i+1, 1, arr, n, dp))
        else:
            profit = max(arr[i] + self.get_profit(i+1, 1, arr, n, dp), 0 + self.get_profit(i+1, 0, arr, n, dp))

        dp[(i, buy)] = profit
        return profit

    def maxProfitII(self, prices): # 122. Best Time to Buy and Sell Stock II (second method)
        n = len(prices)
        profit = 0

        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

    # [4, 1, 3, 3, 2, 3, 1, 1, 4]
    def JumpGameII(self, nums):
        n = len(nums)
        if len(nums) <= 2:
            return len(nums)-1
        l, r, jumps = 0, 0, 0
        while r < n-1:
            farthest = 0
            for index in range(l, r+1):
                ele = nums[index]
                farthest = max(ele + index, farthest)
            l = r + 1
            r = farthest
            jumps += 1
        return jumps

    def trap(self, height: List[int]) -> int: # [4,2,0,3,2,5]
        n = len(height)
        left = [0] * n
        right = [0] * n
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(height[i], left[i-1])
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(height[i], right[i+1])

        total = 0
        for i in range(n):
            total += min(left[i], right[i]) - height[i]
        return total

    def trapMethod2(self, arr):
        leftMax = rightMax = total = 0
        l = 0
        n = len(arr)
        r = n-1
        while l < r:
            if arr[l] <= arr[r]:    
                if leftMax > arr[l]:
                    total += leftMax - arr[l]
                else:
                    leftMax = arr[l]
                l += 1
            else:
                if rightMax > arr[r]:
                    total += rightMax - arr[r]
                else:
                    rightMax = arr[r]
                r -= 1
        return total


sol = Solution()
# print(sol.removeDuplicates([0,0,1,1,1,1,2,3,3]))
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))

# print(sol.canJump_method2([1,1,1,0]))
# print(sol.maxProfit([1,2,3,4,5]))
# print(sol.maxProfitII([1,2,3,4,5]))
# print(sol.JumpGameII([2,3,1,4,1,1,1,2]))

# print(sol.trap(height = [4,2,0,3,2,5]))
print(sol.trapMethod2(arr = [0,1,0,2,1,0,1,3,2,1,2,1]))