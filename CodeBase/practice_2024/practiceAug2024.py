import math
from typing import List


class Solution:
    def list_practice(self):
        og_list =  [x for x in range(1, 21)]
        print("Original List - ", og_list)
        square_list = list(map(lambda x: x**2, og_list))
        print(f"Square List is - {square_list}")
        even_numbers = list(filter(lambda x: x % 2 == 0, square_list))
        print(f"Even number Square List is - {even_numbers}")
        odd_numbers = list(filter(lambda x: x%2 != 0, square_list))
        print(f"Odd Number Square List is - {odd_numbers}")
        squareroot = [int(math.sqrt(x)) for x in square_list]
        print(f"Square root using List comprehension is - {squareroot}")
        squareroot_lambda = list(map(lambda x: int(math.sqrt(x)), square_list))
        print(f"Square roon using filter and lambda on List is - {squareroot_lambda}")
    def lambda_map_filter_prac(self):
        lt = [(4, 5, 8), (3, 2, 6), (8, 9, 10), (8, 8, 8)]
        avg_list = list(map((lambda x: (x[0]+x[0]+x[0])//3), lt))
        print(f"Avg List is - {avg_list}")

        avg_val = lambda x, y, z: (x+y+z)//3
        print("Avg Value - ", avg_val(80, 90, 70))
        print(avg_val)

    def isIsomorphic(self, s: str, t: str) -> bool: # s = "paper", t = "title"
        scharmap = {}
        tcharmap = {}
        for i, ele in enumerate(list(s)):
            skey = ele
            tkey = t[i]
            if (skey in scharmap and scharmap[skey] != tkey) or (tkey in tcharmap and tcharmap[tkey] != skey):
                return False
            else:
                scharmap[skey] = t[i]
                tcharmap[tkey] = skey
        return True

    def isIsomorphicMethod2(self, s, t):
        if len(s) != len(t): return False
        charmap = {}
        used_set = set()
        for schar, tchar in zip(s, t):
            if schar not in charmap:
                if tchar in used_set:
                    return False
                charmap[schar] = tchar
                used_set.add(tchar)
            elif charmap[schar] != tchar:
                return False

        return True

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool: #using set
        nset = set()
        for i, num in enumerate(nums):
            if num in nset:
                return True
            nset.add(num)
            if len(nset) > k:
                nset.remove(nums[i -k ])
        return False

    def containsNearbyDuplicateMethod2(self, nums: List[int], k: int) -> bool: #using Dict
        n_to_i = {}
        for i, n in enumerate(nums):
            if n in n_to_i and abs(i-n_to_i[n] <= k):
                return True
            n_to_i[n] = i
        return False

    def isPowerOfTwo(self, n: int) -> bool: #check if power of 2 using binary search
        r = 31
        l = 0
        if n == 1:
            return True
        return self.get_power(n, l, r, n)

    def get_power(self, n, l, r, ele): #recursive calls
        if l > r:
            return False
        mid = (l + r) // 2
        if ele == 2**mid:
            return True
        elif ele > 2 ** mid:
            return self.get_power(n, mid+1, r, ele)
        else:
            return self.get_power(n, l, mid-1, ele)

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n+1):
            total += i
        actual = (n * (n + 1)) // 2
        return actual - total

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        fast, slow = 1, 0
        while fast < len(nums):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            elif nums[slow] != 0:
                slow += 1
            fast += 1
        print(nums)



if __name__ == '__main__':
    sol = Solution()
    # sol.list_practice()
    # sol.lambda_map_filter_prac()
    # print(sol.isIsomorphicMethod2(s="BADC", t="BABA"))
    # print(sol.containsNearbyDuplicateMethod2(nums = [1,0,1,1], k = 1))

    print(sol.moveZeroes([1,0,1]))