class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_to_t = {}
        t_to_s = {}
        for chars, chart in zip(s, t):
            if chars in s_to_t:
                if s_to_t[chars] != chart:
                    return False
            else:
                if chart in t_to_s:
                    return False
            s_to_t[chars] = chart
            t_to_s[chart] = chars
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isIsomorphic(s = "egg", t = "add"))