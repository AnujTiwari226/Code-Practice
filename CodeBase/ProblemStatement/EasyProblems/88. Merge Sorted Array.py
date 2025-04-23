from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Eg .
        Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        Output: [1,2,2,3,5,6]
        """
        if n == 0:
            return
        end_idx = len(nums1)-1
        while n > 0 and m > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[end_idx] = nums1[m-1]
                m -= 1
            else:
                nums1[end_idx] = nums2[n-1]
                n-=1
            end_idx -=1
        while n > 0:
            nums1[end_idx] = nums2[n-1]
            end_idx-=1
            n-=1


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(nums1)
    sol.merge(nums1=nums1, m=m, nums2=nums2, n=n)
    print(nums1)
    print()
