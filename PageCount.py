class Solution:

    def page_count(self, n, p):
        """
        problem - https://www.hackerrank.com/challenges/drawing-book/problem

        :param n:the number of pages in the book
        :param p:the page number to turn to

        :return: the minimum number of pages to turn
        """
        front = p // 2
        back = n // 2 - front
        return min(front, back)


if __name__ == "__main__":
    """
    In this Drawing Book problem you have Given n and p, 
    find and print the minimum number of pages that must be turned in in order to arrive at page p.
    
    """
    print("Enter no of pages 1st and then target page : ")
    n = int(input().strip())
    p = int(input().strip())
    sol = Solution()
    print(sol.page_count(n, p))
