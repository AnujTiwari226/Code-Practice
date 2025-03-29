from typing import List


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Rearranges the list of integers into the next lexicographically greater permutation.

        If such arrangement is not possible (i.e., the array is in descending order),
        it transforms the list into the lowest possible order (i.e., sorted in ascending order).

        The transformation is done in-place with O(n) time complexity and O(1) extra space.

        Steps:
        1. Find the first index `idx` from the right such that nums[idx] < nums[idx + 1].
           This marks the pivot where the descending sequence begins.
        2. If no such index exists, reverse the entire list (last permutation case).
        3. Otherwise, find the smallest number to the right of `idx` that is larger than nums[idx],
           and swap them.
        4. Reverse the subarray from idx + 1 to end to get the next smallest permutation.

        Parameters:
        nums (List[int]): List of integers to be rearranged.
        """

        idx = -1
        n = len(nums)
        # Step 1: Find the first decreasing element from the right
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                idx = i
                break
        # Step 2:  If no such element, it's the last permutation
        if idx == -1:
            nums.reverse()
            return
        # Step 3: Find the next greater element to the right of idx
        for i in range(n-1, idx-1, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break;
        nums[idx+1:] = reversed(nums[idx+1:])


if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,2]
    print(f'before -> nums = {nums}')
    sol.nextPermutation(nums)
    print(f'before -> nums = {nums}')