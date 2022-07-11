from collections import Counter


class Solution:

    @staticmethod
    def sock_merchant_1(n, ar):
        """
        Using loop to iterate through the arr and dict to store socks as
        keys and number of socks as values

        :param n:the number of socks in the pile
        :param ar:the colors of each sock
        :return: return an integer representing the number of matching pairs of socks that are available
        """
        # Write your code here
        count = 0
        pairs = {}
        for p in ar:
            if p in pairs.keys():
                pairs[p] += 1
            else:
                pairs[p] = 1
        for value in pairs.values():
            pair = value // 2
            if pair > 0:
                count += pair

        return count

    def sock_merchant_2(self, n, arr):
        """
        Using Collection.Counter method

        :param n:the number of socks in the pile
        :param ar:the colors of each sock
        :return: return an integer representing the number of matching pairs of socks that are available
        """

        count_dict = Counter(arr)
        return sum(i // 2 for i in count_dict.values())


if __name__ == "__main__":
    """
        HackerRank Problem

        Given an array of integers representing the color of each sock,
        determine how many pairs of socks with matching colors there are.
        
        We'll be solving it using 2 methods
        1.  Using loop to iterate through the arr and dict to store socks as keys and number of socks as values
        2. Counter method
        eg . 
            n = 9
            arr = 10 20 20 10 10 30 50 10 20
    """
    n = input()
    arr = list(map(int, input().split()))
    sol = Solution()
    print(sol.sock_merchant_1(n, arr))
    print(sol.sock_merchant_2(n, arr))
