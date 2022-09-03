from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            val1 = nums[i]
            val2 = nums[val1]
            result.append(val2)

        return result


if __name__ == '__main__':
    nums = [5,0,1,2,3,4]
    sol = Solution()
    print(sol.buildArray(nums))
