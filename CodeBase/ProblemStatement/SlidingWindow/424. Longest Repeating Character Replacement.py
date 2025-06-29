from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        left = 0
        char_count = defaultdict(int)
        maxl = 0
        for r in range(len(s)):
            char_count[s[r]] += 1
            maxf = max(maxf, char_count[s[r]])

            if (r - left + 1) - maxf > k:
                char_count[s[left]] -= 1
                left += 1
            maxl = max(maxl, r - left + 1)
        return maxl

if __name__ == '__main__':

    sol = Solution()
    print(sol.characterReplacement(s = "AABABBA", k = 1))
