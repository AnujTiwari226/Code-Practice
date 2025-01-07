from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        for i in range(len(nums)):
            zeros = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    zeros += 1
                if zeros <= k:
                    curr = j - i + 1
                    max_len = max(curr, max_len)
                else:
                    break
        return max_len
    
    def longestOnes_Optimal(self, nums: List[int], k: int) -> int: # time complexity = o(2n)
        max_len = 0
        left = 0
        zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len
    
    def longestOnes_MostOptimal(self, nums: List[int], k: int) -> int:
        max_len = 0
        left = 0
        zeros = 0
        if nums.count(0) <= k:
            return len(nums)
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros == k:
                max_len = max(max_len, right - left + 1)

        return max_len
if __name__ == '__main__':
    sol = Solution()
    print(sol.longestOnes_MostOptimal(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
