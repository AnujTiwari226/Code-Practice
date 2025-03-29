import time


class Solution:
    def longestSubarray(self, arr, k):
        maxl = 0
        l = 0

        while l < len(arr):
            r = l
            curr_sum = 0
            while r < len(arr):
                curr_sum += arr[r]
                if curr_sum == k:
                    maxl = max(maxl, r - l + 1)
                r += 1
            l+=1
        return maxl

    def longestSubarray_Optimal(self, arr, k):
        prefix = {0:-1}
        curr_sum = 0
        len_max = 0
        for i, num in enumerate(arr):
            curr_sum += num
            if curr_sum == k:
                len_max = max(len_max, i+1)
            if curr_sum - k in prefix:
                len_max = max(len_max, i - prefix[curr_sum-k])
            if curr_sum not in prefix:
                prefix[curr_sum] = i
        return len_max


if __name__ == '__main__':
    sol = Solution()
    arr = [-5, 8, -14, 2, 4, 12]
    k = -5
    # ans = sol.longestSubarray(arr, k)
    print(sol.longestSubarray_Optimal(arr, k))

