import time


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        visited.add(n)
        if n == 1:
            return True
        return self.get_isHappy(n, visited)
        # sum1 = self.get_square_of_digits(n)
        # if sum1 not in visited:
        #     visited.add(sum1)
        #     sum1 = self.sumHappy(sum1)

    def get_isHappy(self, n, visited):
        if n == 1:
            return True
        else:
            temp = 0
            while n > 0:
                temp += (n % 10) ** 2
                n = n // 10
            if temp not in visited:
                visited.add(temp)
                if temp > 9 or temp != 1:
                    return self.get_isHappy(temp, visited)
                else:
                    return True

            else:
                return False


    def get_square_of_digits(self, n):
        temp = 0
        while n > 0:
            temp += (n % 10) ** 2
            n = n // 10
        return temp



    def isHappyOptimized(self, n):
        visited = set()
        def happy(m):
            if m == 1:
                return True
            if m in visited:
                return False
            visited.add(m)
            sumn = 0
            while m // 10 > 0:
                digit = m % 10
                sumn += digit*digit
                m = m // 10
            sumn += (m % 10)**2
            return happy(sumn)
        return happy(n)

sol = Solution()
start = time.time()
print("Result : ", sol.isHappy(19))
end = time.time()
print("time taken ", end - start)
start = time.time()
print("Result in optimized method: ", sol.isHappyOptimized(7))
end = time.time()
print("time taken ", end - start)