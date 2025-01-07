from typing import List


class Solution:

    def get_concatenated_array(self, nums: List[int]) -> List[int]:
        return 2*nums

    def get_concat_array(self, nums: List[int]) -> List[int]:
        ans = nums
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans


sol = Solution()
print(sol.get_concatenated_array([1,2, 3]))
print(sol.get_concat_array([1,2, 3]))