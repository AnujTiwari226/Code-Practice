from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for ele in s:
            freq[ele] += 1
        res = ''
        sorted_freq = sorted(freq.items(), key=lambda v: v[1], reverse=True)
        for key, value in sorted_freq:
            res += key * value

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.frequencySort('AbbacccB'))
