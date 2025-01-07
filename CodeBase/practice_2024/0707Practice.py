import functools
import time
from typing import List


def log_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Total time taken to execute {func.__name__} is [{end - start}]")

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        half = 0
        while x > half:
            half = (half * 10) + (x % 10)
            x = x // 10
        return x == half or x == half // 10
    def romanToInt(self, s: str) -> int:
        keys = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s) - 1):
            vi, vi1 = s[i], s[i+1]
            if keys[s[i]] < keys[s[i+1]]:
                total -= keys[s[i]]

            else:
                total += keys[s[i]]
        return total + keys[s[-1]]
    def romanToIntUsingEnumrate(self, s: str) -> int:
        keys = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
        total = 0
        for index, char in enumerate(s):
            if index == len(s) - 1:
                total += keys[char]
            elif keys[char] < keys[s[index+1]]:
                total -= keys[char]
            else:
                total += keys[char]
        return total

    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        for i in range(1, len(strs)):
            temppref = ''
            letter = strs[i]
            for index, char in enumerate(letter):
                if pref[index] == char:
                    temppref += char
                else:
                    pref = temppref
                    break
            if len(temppref)<=0:
                pref = temppref
                break
        return pref
    def longestCommonPrefixII(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[len(strs)-1]
        pref = ''
        for index, char in enumerate(last):
            if index > len(first)-1:
                break
            if first[index] == char:
                pref += char
            else:
                break
        return pref

    def isValid(self, s: str) -> bool:
        stack = []
        flag = False
        for b in s:
            if b in ['(', '[', '{']:
                stack.append(b)
            else:
                if not stack:
                    return False
                ele = stack.pop()
                if (ele == '(' and b == ')') or ( ele == '[' and b == ']') or (ele == '{' and b == '}'):
                    flag = True
                else:
                    return False
        if len(stack) == 0 and flag:
            return True
        return False

    def searchInsert(self, nums: List[int], x: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == x:
                return  mid
            elif nums[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        # return low if nums[low] - x > nums[high] else high
        return low

    def lengthOfLastWord(self, s: str) -> int:
        list1 = s.strip().split(" ")
        return len(list1[-1])

    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while digits[i] == 9 and i > 0:
            digits[i] = 0
            i -= 1
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            digits.insert(0, 1)
            return digits

    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left<=right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid -1
            else:
                left = mid + 1
        return right
    #@log_time
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        m1, m2, total = 1, 1, 0
        for i in range(2, n+1):
            total = m1 + m2
            m2 = m1
            m1 = total
        return total
    def __init__(self):
        self.memo = {}

    @log_time
    def fibonnaciSeriesSumofN(self, n):
        if n <= 2:
            return n
        if n in self.memo:
            return self.memo[n]
        else:
            f = self.fibonnaciSeriesSumofN(n-1) + self.fibonnaciSeriesSumofN(n-2)
            self.memo[n] = f
            return f

sol = Solution()


# print(sol.isPalindrome(121))

# print(sol.romanToInt('MCMXCIV'))
# print(sol.romanToIntUsingEnumrate('MCMXCIV'))

# strs = ["flower","flow","flight"]
# print('Prefix: ', sol.longestCommonPrefixII(strs))

# print(sol.isValid('({{{{}}}))'))

# nums = [1,3,5,6]
# target = 4
# print(sol.searchInsert(nums, target))

# print(sol.lengthOfLastWord("   fly me   to   the moon  "))

# print(sol.plusOne([7, 9,7, 9,9 ]))

# print(sol.mySqrt(69))

print(sol.climbStairs(3000129))
print(sol.fibonnaciSeriesSumofN(3000021))