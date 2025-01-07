from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr, prev, index = 1, 0, 1
        req_len = 1
        while curr < len(nums):
            curr_val = nums[curr]
            prev_val = nums[prev]
            if nums[curr] != nums[prev]:
                req_len += 1
                nums[index]  = nums[curr]
                index += 1
                prev = curr
            else:
                prev += 1
            curr += 1
        return req_len
    
    def removeDuplicates_Better(self, nums: List[int]) -> int:
        index = 0
        for curr in range(1, len(nums)):
            if nums[index]!=nums[curr]:
                index += 1
                nums[index] = nums[curr]
        return index+1
        



if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates_Better([1,1,2]))