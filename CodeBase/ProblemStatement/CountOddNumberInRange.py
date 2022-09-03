class Solution:
    def count_odd_number_1(self, low, high):
        nums = high - low + 1
        if high % 2 != 0 and low % 2 != 0:
            return nums // 2 + 1
        return nums // 2

    def count_odd_number_2(self, low, high):
       return high // 2 - low // 2


print("Approach 1")
print(Solution().count_odd_number_1(3, 12))
print(Solution().count_odd_number_1(2, 10))
print(Solution().count_odd_number_1(1, 3))


print("Approach 2")
print(Solution().count_odd_number_2(3, 12))
print(Solution().count_odd_number_2(2, 10))
print(Solution().count_odd_number_2(1, 3))


