"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""
from collections import defaultdict
from typing import List


class Solution:

    def subarraySum(self, nums: List, k:int) -> int:

        """
            This method finds the total number of **continuous subarrays** whose sum equals to a given value k.

            The function uses a defaultdict to keep track of the cumulative sum frequencies. This helps in
            determining the number of times a particular cumulative sum has occurred, which in turn helps
            in finding the subarrays with the desired sum.

            The defaultdict is used over a normal dictionary because it automatically initializes any
            missing keys with a default value (in this case, 0). This eliminates the need for additional
            checks to see if a key exists in the dictionary before updating its value.

            We initialize the defaultdict with {0: 1} to handle the case where a subarray that starts from
            the beginning has a sum equal to k. This is because if we encounter a cumulative sum that is
            exactly equal to k, it means we have found a valid subarray.

            :param nums: List[int] - A list of integers representing the input array.
            :param k: int - The target sum for the subarrays.
            :return: int - The total number of continuous subarrays whose sum equals k.

        """
        subarray_sum = 0
        prefix = defaultdict(int)
        prefix[0]=1
        result = 0

        for i in range(len(nums)):
            subarray_sum += nums[i]
            diff = subarray_sum - k
            result += prefix.get(diff, 0)

            prefix[subarray_sum] += 1
        return result


if __name__ == '__main__':
    sol= Solution()
    print(sol.subarraySum(nums = [1, 1, 1, 3, 4, 2, 2, 4], k = 3))

