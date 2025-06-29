class Solution:
    def is_valid(self, s: str) -> bool:
        if not s:
            return False
        stack = []
        md = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in md:
                stack.append(c)
            elif len(stack) == 0 or md[stack.pop()] != c:
                return False
        return len(stack) == 0

if __name__ == '__main__':
    s = Solution()
    print(s.is_valid('()[]{}'))