# stock=[]
"""
30 days of prices, list ofi prices, what price to buy/ sell and maxp
we can sell and buy anyday
st = []
"""



class Solution:

    def max_profit_daily(self, prices):
        if not prices:
            return 0
        prof = 0
        for i in range(1, len(prices)):
            temp = 0
            if prices[i] > prices[i-1]:
                prof += prices[i] - prices[i-1]
        return prof


if __name__ == '__main__':
    sol = Solution()
    print(sol.max_profit_daily([1, 2, 3, 0, 5, 6]))

    """
    buy 1st - 0th
    sell on 2nd 
    """
