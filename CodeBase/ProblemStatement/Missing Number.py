class Solution:
    def missingNumber(self, nums):
        actual, expected = 0, 0
        for ele in nums:
            actual += ele
        expected = (len(nums) * (len(nums) + 1)) // 2
        return expected - actual


if __name__ == '__main__':
    sol = Solution()
    print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))