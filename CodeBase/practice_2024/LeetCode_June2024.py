from asyncio.log import logger
from typing import List


class Solution:

    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        if len(nums)==0:
            return []
        elif len(nums) == 1 and nums[0] == val:
            return []
        else:
            i=0
            for j in range (len(nums)):
                if nums[j] != val:
                    nums[i] = nums[j]
                    i+=1
            return i

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
           return 0
        if len(needle) > len(haystack):
            return -1
        ln = len(needle)
        n = len(haystack)
        value_of_range = n - ln + 1
        for j in range(value_of_range):
            ele = haystack[j:j+ln]
            if ele == needle:
                return j
        return -1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m-1, n-1, m+n-1
        while j>= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

    def isPalindrome(self, s: str) -> bool:
        if len(s) < 1:
            return False
        i = 0
        j = len(s) - 1
        while i <= j:
            elei = s[i]
            elej = s[j]
            if not elei.isalnum():
                i += 1
            elif not elej.isalnum():
                j -= 1
            else:
                if elei.lower() != elej.lower():
                    return False
                j -= 1
                i += 1
        return True


nums = [1]
val = 1
expectedNums = Solution.removeElement(nums, val)

print("expected nums", expectedNums)

haystack = "mississippi"
needle = "issip"

obj = Solution()
ans = obj.strStr(haystack, needle)
print(ans)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
obj.merge(nums1, m, nums2, n)
for ele in nums1:
    print(ele, end=" ")
print('')

#strs = "A man, a plan, a canal: Panama"
#strs = "race a car"
strs = "D@! a d@"
print(obj.isPalindrome(strs))