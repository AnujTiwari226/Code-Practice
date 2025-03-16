

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.
        
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]

        Args:
            nums (List[int]): list of integers 

        Returns:
            List[List[int]]: list of unique triplets
        """
        result = set()
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums) - 1
            temp = []
            while(left < right):
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    temp = (nums[i], nums[left], nums[right])
                    result.add(temp)
                    right -= 1
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return result
    
    def threeSum_BetterApproach(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: 
            return []
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while(left < right and nums[left] == nums[left+1]):
                        left += 1
                    while(left < right and nums[right] == nums[right-1]):
                        right -= 1
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return [list(triplet) for triplet in result]

if __name__ == '__main__':
    sol = Solution()
    # print(sol.threeSum([-1,0,1,2,-1,-4]))
    print(sol.threeSum_BetterApproach([-1,0,1,2,-1,-4]))