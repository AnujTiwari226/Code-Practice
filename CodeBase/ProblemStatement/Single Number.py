class Solution:
    def singleNumber(self, nums):
        """
         using XOR where
         a ^ a = 0,
         a ^ 0 = a,
         a ^ b = a+b,
         (a+b) ^ a = b
        :param nums:
        :return: number occurring only once
        """
        res = 0
        for num in nums:
            res = res ^ num
        return res

    def singleNumber_set(self, nums):
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return list(s)[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber_set(nums = [4, 2, 2, 3, 1, 3, 1, 5, 4]))
