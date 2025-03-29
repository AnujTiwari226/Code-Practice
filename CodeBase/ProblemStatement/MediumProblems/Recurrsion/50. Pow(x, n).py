class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return x

        def helper(x, n):
            if n == 0:
                return 1
            x = x * helper(x, n - 1)
            return x

        if n < 0:
            n = abs(n)
            val = helper(x, n)
            return 1 / val
        else:
            val = helper(x, n)
            return val


    def myPow_optimal(self, x, n):
        def helper(x, n):
            if n == 0:
                return 1
            half = helper(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return x * half * half
        if n < 0:
           return 1 / helper(x, -n)
        else:
            return helper(x, n)


if __name__ == '__main__':
    sol = Solution()
    x = 2.00000
    n = 10
    print(sol.myPow_optimal(x, n))