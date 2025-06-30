class Solution:
    def largestOddNumber(self, num: str) -> str:
        ele = num[-1]
        if int(ele) % 2 != 0:
            return num
        res = ''
        for i in range(len(num)):
            if int(num[i]) % 2 != 0:
                res = num[:i+1]
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.largestOddNumber('52'))