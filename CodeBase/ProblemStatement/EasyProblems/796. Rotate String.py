class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        sl = list(s)

        if len(s) != len(goal):
            return False
        if not s:
            return True
        for _ in range(len(sl)):
            temp = sl.pop(0)
            sl.append(temp)
            if ''.join(sl) == goal:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.rotateString(s = "abcde", goal = "cdeab"))
