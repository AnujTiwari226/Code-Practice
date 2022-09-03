class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n == 0:
        #     return False
        # rem = n % 3
        # q = n//3
        # if rem == 0 and q % 3 == 0:
        #     return True
        # return False
        return n > 0 and (n == 1 or (n % 3 == 0 and self.isPowerOfThree(n//3)))


print(Solution().isPowerOfThree(45))

print(Solution().isPowerOfThree(81))