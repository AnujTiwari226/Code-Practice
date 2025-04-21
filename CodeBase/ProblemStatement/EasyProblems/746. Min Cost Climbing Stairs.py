from typing import List


class Solution:

    def minCostClimbingStairs_EasyApproach(self, cost: List[int]) -> int:
        n = len(cost)
        cost0 = cost[0]
        cost1 = cost[1]
        total = cost1
        for i in range(2, n):
            total = cost[i] + min(cost0, cost1)
            cost0 = cost1
            cost1 = total
        return min(cost0, total)

    def minCostClimbingStairs_DPApproach(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1)
        def helper(idx):
            if idx >= n:
                return 0
            if dp[idx] != -1: return dp[idx]
            left = cost[idx] + helper(idx+1)
            right = cost[idx] + helper(idx+2)
            dp[idx] = min(left, right)
            return dp[idx]
        return min(helper(0), helper(1))


if __name__ == '__main__':
    sol = Solution()
    print(f"Using Easy approach - {sol.minCostClimbingStairs_EasyApproach([1,100,1,1,1,100,1,1,100,1])}")
    print(f"Using dp approach - {sol.minCostClimbingStairs_DPApproach([1,100,1,1,1,100,1,1,100,1])}")