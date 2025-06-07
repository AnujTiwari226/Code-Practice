from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort the intervals based on their first ele so that we can get the intervals in a seq
        then ->
        check if the last ele of last array in merged is less than 1st element of current inter
            if yes then no overlapping - eg
                merged = [[1, 6], [8, 10]] and current inter = [11, 16] then 10 < 11 so there is no overlap
            Append the inter directly
            otherwise ->
                we need to get the max of = last ele of last array from merged and last ele of inter
                e.g. merged = [[1, 3]] and current inter = [2, 5] then here 3 is not less than 2 so overlap is happening
                in such cases, we'll pick max(3, 5) and update merged's last array's last ele i.e. merged = [[1. 5]]
        :param intervals:
        :return: 
        """
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x[0])
        merged = []
        for inter in intervals:
            if not merged or merged[-1][1] < inter[0]:
                merged.append(inter)
            else:
                merged[-1][1] = max(merged[-1][1], inter[1])

            # debug purpose
            # if merged[-1][1]:
            #     ele = merged[-1][1]
        return merged


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    sol = Solution()
    print(sol.merge(intervals))