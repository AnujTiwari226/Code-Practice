class Solution:
    def jump(self, nums):
        n = len(nums)
        if n <= 2:
            return n-1
        current, jumps, farthest = 0, 0, 0
        for i in range(n-1):
            farthest = max(farthest, i+nums[i])
            if i == current:
                jumps += 1
                current = farthest
                if current >= n-1:
                    break
        return jumps


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 3, 1, 1, 4, 2, 0, 1, 4]
    print(sol.jump(nums))