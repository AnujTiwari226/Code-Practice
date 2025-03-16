"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees
excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
"""
from typing import List


def avg_salary(nums: List[int]) -> int:
    min = max = total = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < min:
            min = nums[i]
        if nums[i] > max:
            max = nums[i]
        total += nums[i]
    return (total-min-max) // (len(nums) - 2)



print(avg_salary([100, 1000, 4000, 7000]))

