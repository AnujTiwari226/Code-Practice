class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1 and s[0] == " ":
            return ""

        words = s.strip().split()
        words.reverse()
        return ' '.join(words)


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords("  hello   world  "))