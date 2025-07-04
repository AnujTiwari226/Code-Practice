class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        if not s or len(s) == 1:
            return s
        longest = ''
        for i in range(len(s)):
            odd = expand_from_center(i, i)
            even = expand_from_center(i , i+1)
            if len(longest) < len(odd): longest = odd
            if len(longest) < len(even): longest = even

        return longest


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome("cbbd"))