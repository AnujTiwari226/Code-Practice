from collections import defaultdict
from typing import List


class Solution:
    def majorityElement_better(self, nums: List[int]) -> List[int]:
        ls = []
        d = defaultdict(int)
        minn = (len(nums) // 3) + 1

        for num in nums:
            d[num] += 1
            if d[num] == minn:
                ls.append(num)
            if len(ls)  == 2:
                break
        return ls

    def majorityElement_optimal(self, nums: List[int]) -> List[int]:
        cnt1, cnt2 = 0, 0
        ele1, ele2 = float('-inf'), float('-inf')
        for num in nums:
            if cnt1 == 0 and num != ele2:
                cnt1 += 1
                ele1 = num
            elif cnt2 == 0 and num != ele1:
                cnt2 += 1
                ele2 = num
            elif ele1 == num:
                cnt1 += 1
            elif ele2 == num:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1, cnt2 = 0, 0
        for num in nums:
            if ele1 == num: cnt1+=1
            if ele2 == num: cnt2+=1
        minn = (len(nums) // 3) + 1
        ls = []
        if cnt1 >= minn: ls.append(ele1)
        if cnt2 >= minn: ls.append(ele2)
        return ls


if __name__ == '__main__':
    sol = Solution()
    inps = [[1,2], [3,2,3], [1]]
    for num in inps:
        print(sol.majorityElement_optimal(num))



