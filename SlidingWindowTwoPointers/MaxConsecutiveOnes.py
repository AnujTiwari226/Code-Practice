from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxlen = 0 
        l = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                l += 1
            else:
                maxlen = max(l, maxlen)
                l = 0
            i+=1
        return max(maxlen, l)
# or 
    def findMaxConsecutiveOnes_Optimal(self, nums: List[int]) -> int:
        maxlen = 0 
        ln = 0
        for num in nums:
            if num == 1: # can also compare with a value like target
                ln += 1
                maxlen = max(maxlen, ln)
            else:
                ln = 0
        return maxlen

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))
    print("Optimal: ", sol.findMaxConsecutiveOnes_Optimal(nums = [1,0,1,1,0,1]))