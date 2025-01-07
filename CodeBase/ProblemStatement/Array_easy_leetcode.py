from typing import List


class Solution:

    def get_ruuning_sum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dict = {'--X': -1, '++X': 1, 'X--': -1, 'X++': 1}
        X = 0
        for s in operations:
            X += dict[s]
        return X

    def get_maximum_wealth(self, accounts: List[List[int]]) -> int:
        max_wealth= 0
        for i in range(len(accounts)):
            temp_arr = accounts[i]
            temp_max = 0
            for j in range(len(temp_arr)):
                temp_max += temp_arr[j]
            max_wealth = temp_max if max_wealth <= temp_max else max_wealth

        return max_wealth

    def shuffle(self, nums: List[int], n:int) -> List[int]:
        res = []
        i = 0
        while i <= n-1:
            res.append(nums[i])
            res.append(nums[i+n])
            i += 1
        return res

    def shuffle_inplace(self, nums: List[int], n: int) -> List[int]:
        for i in range(n, n*2):
            nums[i] = nums[i]*1024 + nums[i-n]
        index = 0
        for i in range(n, n*2):
            nums[index] = nums[i] % 1024
            nums[index+1] = nums[i] // 1024
            index += 2
        return nums

    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for ele in sentences:
            temp = ele.count(' ') + 1
            if count <= temp:
                count = temp
        return count

    def num_identical_pair(self, nums: List[int]) -> int:
        no_of_pairs = 0
        for i in range(0, len(nums)-1):
            ele_i = nums[i]
            for j in range(i+1, len(nums)):
                ele_j = nums[j]
                if ele_i == ele_j:
                    no_of_pairs += 1
        return no_of_pairs

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        for i in range(0, len(candies)):
            total = candies[i] + extraCandies
            flag = True
            for j in range(0, len(candies)):
                if candies[j] > total:
                    flag = False
            output.append(flag)
        return output


    def kidsWithCandiesOptimal(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        maximum = max(candies) - extraCandies
        for candy in candies:
            output.append(maximum <= candy)
        return output

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0, len(nums)):
            count = 0
            for j in range(0, len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            output.append(count)
        return output

    def smallerNumbersThanCurrentOptimal(self, nums: List[int]) -> List[int]:
        buckets = [0] * 101
        for num in nums:
            buckets[num] += 1
        previous = 0
        for i, bucket in enumerate(buckets):
            if bucket != 0:
                buckets[i] = previous
                previous += bucket
        return [buckets[num] for num in nums]

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for j in jewels:
            for s in stones:
                if j == s:
                    count += 1
        return count



if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 1]
    print("Running sum of %s: ", nums)
    print("Running sum is %s", sol.get_ruuning_sum(nums))

    print("---------Problem 2--------- \nFinalValueAfterOperation :- ")
    print(sol.finalValueAfterOperations(["X++","++X","--X","X--"]))

    print("---------Problem 3--------- \nFind Richest Customer Wealth :- ")
    print(sol.get_maximum_wealth([[1, 2, 3], [3, 4, 5], [1, 1, 1, 1, 4]]))

    print("---------Problem 4---------\nShuffle the Array :- ")
    print(sol.shuffle(nums=[2, 5, 4, 3], n=2))
    print(sol.shuffle_inplace(nums=[2, 5, 4, 3, 4, 5], n=3))

    print("---------Problem 5---------\nMost word found :- ")
    print(sol.mostWordsFound(["please wait", "continue to fight", "continue to win"]))

    print("---------Problem 6---------\nIdentical pairs :- ")
    print(sol.num_identical_pair([1, 1, 1, 1]))

    print("---------Problem 7---------\nKids With the Greatest Number of Candies :- ")
    print(sol.kidsWithCandies([2,3,5,1,3], 3))
    print('Sol2: ', sol.kidsWithCandiesOptimal([2,3,5,1,3], 3))
    print(sol.num_identical_pair([1, 1, 1, 1]))

    print("---------Problem 8---------\nHow Many Numbers Are Smaller Than the Current Number :- ")
    print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))
    print(sol.smallerNumbersThanCurrentOptimal([8,1,2,2,3]))

    print("---------Problem 9---------\nJewels and Stones :- ")
    print(sol.numJewelsInStones('Aa', 'aAAAaDDD'))

