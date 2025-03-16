from typing import List


class Solution:
    def get_initial_energy(self, arr):
        initial_energy = 0
        curr = 0
        flag = 0
        n = len(arr)
        for i in range(n):
            curr += arr[i]
            if curr <= 0:
                initial_energy += (abs(curr) + 1)
                curr = 1
                flag = 1
        return 1 if flag == 0 else initial_energy

    def checkIfUnequal(self, l, r, q):
        total = 0
        for num in range(l, r+1):
            product = num * q
            print(f"num - {num} *  and Product is -  {product}")
            snum = str(num)
            sprod = str(product)

            if not any(char in sprod for char in snum):
                print(product)
                total += 1
        return total

    def decodeString(self, s: str) -> str:
        curr_str, snum = '', 0
        stack = []
        for char in s:
            if char.isdigit():
                snum += snum*10 + int(char)
            elif char == '[':
                stack.append(curr_str)
                stack.append(int(snum))
                curr_str = ''
                snum = 0
            elif char == ']':
                prev_num = stack.pop()
                prev_char = stack.pop()
                curr_str = prev_char + prev_num*curr_str
            else:
                curr_str += char
        return curr_str

    def compress(self, chars: List[str]) -> int:
        res = []
        curr_str, count = chars[0], 1
        i = 1
        while i < len(chars):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                res.append(curr_str)
                if count > 1:
                    num = list(str(count))
                    res.extend(num)
                curr_str = chars[i]
                count = 1
            i += 1
        if count > 1:
            res.append(curr_str)
            num = list(str(count))
            res.extend(num)
        print(res)
        return len(res)

    def compressMethodII(self, arr):
        i = 0
        ans = 0
        while i < len(arr):
            char = arr[i]
            count = 0
            while i < len(arr) and arr[i] == char:
                count += 1
                i += 1
            arr[ans] = char
            ans += 1
            if count > 1:
                for c in str(count):
                    arr[ans] = c
                    ans += 1
            return ans

    def encode(self, s: str) -> str:
        # code here
        i, ans = 0, 0
        n = len(s)
        res = []
        while i < n:
            char = s[i]
            count = 0
            while i < n and s[i] == char:
                count += 1
                i += 1
            res.append(char)
            res.append(str(count))

        st = ''.join(res)
        print(st)
        return st

    def countWays(self, n, dp):
        if (n <= 1):
            return 1

        if (dp[n] != -1):
            return dp[n]

        dp[n] = self.countWays(n - 1, dp) + self.countWays(n - 2, dp)
        return dp[n]

    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            s = nums[slow]
            f = nums[nums[fast]]
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        finder = nums[0]
        while slow != finder:
            nsf = nums[slow]
            nff = nums[finder]
            slow = nums[slow]
            finder = nums[finder]
        return finder

    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum, res = 0, nums[0]
        for n in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += n
            res = max(res, curr_sum)
        return res

    def find_missing_and_duplicate(self, arr):
        n = len(arr)
        freq = [0] * (n + 1)

        for num in arr:
            freq[num] += 1

        duplicate = -1
        missing = -1

        for i in range(1, n + 1):
            if freq[i] == 2:
                duplicate = i
            elif freq[i] == 0:
                missing = i

        return missing, duplicate


if __name__ == '__main__':

    sol = Solution()
    # print(sol.get_initial_energy(arr = [4, -10 , 4, -14, 4]))
    # print(sol.checkIfUnequal(5, 15, 2))
    # print(sol.decodeString("3[a2[c]]"))

    # print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
    # print(sol.encode('aaaabbbccc'))
    # print(sol.countWays(n=3, dp= [-1 for _ in range(3+1)]))
    # print(sol.findDuplicate([1,3,4,2,2]))
    # print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    arr = [4, 3, 6, 2, 1, 1]
    missing, duplicate = sol.find_missing_and_duplicate(arr)
    print("Missing number:", missing)
    print("Duplicate number:", duplicate)