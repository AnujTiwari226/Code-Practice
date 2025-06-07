# class Solution:
#     def get_pairs(self, nums):
#         n = len(nums)
#         res = 0
#         if not nums and n < 2:
#             return 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 ele_diff = nums[i] - nums[j]
#                 idx = i-j
#                 if ele_diff == idx:
#                      res += 1
#         return res
#     # from collections import Counter
#  zx
#
# # arr = [1, 1, 1, 3, 3, 5]
# @staticmethod
# @classmethod

a = {10: 'a', 20: 'b'}
b = {10: 'a', 20: 'b'}

print(a is b)


# if __name__ == '__main__':
#     nums = [3, 5,1 , 4, 6, 6]
#     nums1 = [2, 7, 4, 5, 6, 7]
#     """
#     1, 3
#     1, 4
#     n+ ... + 5 + 4 + 3 + 2 + 1
#     (N-1)(n) // 2
#     a[i] - i = a[j] - j
#
#     """
#     sol = Solution()
#     print(sol.get_pairs_II(nums))


class XYZ:
    def __init__(self):
        _a = 10
        lst = [i for i in range(10)]

