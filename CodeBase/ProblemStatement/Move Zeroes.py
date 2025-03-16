class Solution:
    def moves_zeros(self, nums):
        if len(nums) < 2:
            return 0
        fast, slow = 1, 0
        while fast < len(nums):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            if nums[slow] != 0:
                slow += 1
            fast += 1


if __name__  == '__main__':
    sol = Solution()
    nums = [0, 1, 0, 3, 12]
    nums1 = [0, 0, 0, 1, 3, 0]
    sol.moves_zeros(nums1)
    print(nums1)
