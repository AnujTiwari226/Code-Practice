from typing import List


# 20231301 and # 20231302
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(0, len(nums)):
            if nums[i] in result.keys():
                return [i, result.get(nums[i])]
            else:
                result[target-nums[i]] = i

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left, right = 0, 1
        while right < len(prices):
            temp = prices[right] - prices[left]
            if prices[left] < prices[right]:
                profit = max(profit, temp)
            else:
                left = right
            right += 1

        return profit

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pm, pn = 0, 0
        while pn < n:
            pm_v, pn_v = nums1[pm], nums2[pn]
            if nums2[pn] <= nums1[pm] or nums1[pm] == 0:
                nums1.insert(pm, nums2[pn])
                nums1.pop()
                pn += 1
                pm += 1
            else:
                pm += 1

    def merge_correct(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m-1, n-1, m+n-1
        while j >= 0:
            n1i = nums1[i]
            n2j = nums2[j]
            if i >= 0 and nums1[i] > nums2[j]:
                nk = nums1[k]
                ni = nums1[i]
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nk = nums1[k]
                nj = nums2[j]
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

    def runningSum(self, nums: List[int]) -> List[int]:
        i = 1
        while i < len(nums):
            nums[i] = nums[i-1]+nums[i]
            i += 1

    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        total_sum = 0
        for n1 in nums:
            total_sum = total_sum+n1
        for i in range(len(nums)):
            if left * 2 == total_sum - nums[i]:
                return i
            else:
                left += nums[i]
        return -1


sol = Solution()
nums = [2, 7, 11, 15]
# print(sol.twoSum(nums, 9))
prices = [7, 1, 5, 3, 6, 4]
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print('after method was called..')
# sol.merge_correct(nums1, m, nums2, n)
# print(nums1)
r_nums = [1, 2, 3, 4]
# sol.runningSum(r_nums)
# print(r_nums)
nums_p = [1, 2, 3]
#print(sol.pivotIndex(nums_p))


# 20231303
class SolutionD3:
    def majorityElement(self, nums: List[int]) -> int:
        merged_list = self.merge_sort(nums)
        return merged_list[len(merged_list)//2]

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        merged_list = []
        while left and right:
            if left[0] <= right[0]:
                merged_list.append(left.pop(0))
            else:
                merged_list.append(right.pop(0))
        merged_list.extend(left or right)
        return merged_list

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return n
        else:
            n1 = list(self.fib_sum(n))
            ele = n1[n]
            return ele

    def fib_sum(self, n):
        x, y = 0,1
        for _ in range(n+1):
            yield x
            x, y = y, y+x

    def fib1(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0], dp[1] = 0, 1
        for i in  range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

    def sortedSquares(self, nums: List[int]) -> List[int]:
        # brute force
        # llist = [0] * (len(nums))
        # pidx = -1
        # for index, ele in enumerate(nums):
        #     llist[index] = ele * ele
        # print(llist)
        # llist.sort()
        # return llist
        start, end = 0, len(nums)-1
        res = [0] * len(nums)
        reset = end
        while start <= end:
            if nums[start]*nums[start] > nums[end] * nums[end]:
                res[reset] = nums[start]*nums[start]
                reset -= 1
                start += 1
            else:
                res[reset] = nums[end] * nums[end]
                reset -= 1
                end -= 1

        return res

    def removeDuplicates(self, nums: List[int]):
        i, j = 0, 1
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
        count = i+1
        return nums


sol3 = SolutionD3()
numsMaj = [2,2,1,1,1,2,2]
# print(sol3.majorityElement(numsMaj))
n = 3
# print(sol3.fib(n))
# print(sol3.fib1(5))
# print(sol3.sortedSquares(nums=[-7,-3,2,3,11]))
print(sol3.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))