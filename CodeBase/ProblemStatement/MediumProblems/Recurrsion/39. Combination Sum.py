from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in `candidates` where the numbers sum to `target`.
        Each number in `candidates` may be used unlimited number of times.

        Approach:
            - Uses a backtracking (pick/not pick) approach to explore all possible combinations.
            - For each candidate, we have two choices:
                1. Pick the current candidate (if it doesn't exceed the remaining target)
                   - Add it to the current combination (`ds`)
                   - Recursively continue with the same candidate (since reuse is allowed)
                   - Subtract the candidate's value from the remaining target
                2. Skip the current candidate
                   - Move to the next candidate without changing the target

        Base Case:
            - When we've processed all candidates (`idx == len(candidates)`):
                - If the remaining target is 0, we've found a valid combination (add to `res`)
                - Otherwise, backtrack

        Parameters:
            candidates (List[int]): List of distinct integers to choose from
            target (int): The desired sum for combinations

        Returns:
            List[List[int]]: All unique combinations that sum to `target`

        Example:
            combinationSum([2,3,6,7], 7)
            [[2,2,3], [7]]
        """
        res = []
        n = len(candidates)

        def helper(idx: int, target: int, ds: List[int]) -> None:
            """
            Backtracking helper function.

            Args:
                idx: Current index in candidates list
                target: Remaining sum needed
                ds: Current combination being built
            """
            if idx == n:
                if target == 0:
                    res.append(ds.copy())
                return

            # Pick current candidate (if valid)
            if candidates[idx] <= target:
                ds.append(candidates[idx])
                helper(idx, target - candidates[idx], ds)
                ds.pop()  # Backtrack

            # Don't pick current candidate
            helper(idx + 1, target, ds)

        helper(0, target, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([2,3,6,7], 7))