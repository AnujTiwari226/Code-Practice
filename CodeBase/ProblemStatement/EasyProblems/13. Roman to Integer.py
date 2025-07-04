class Solution:
    def romanToInt(self, s: str) -> int:
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


if __name__ =='__main__':
    sol = Solution()
    print(sol.romanToInt(s = "III"))
    print(sol.romanToInt(s = "MCMXCIV"))