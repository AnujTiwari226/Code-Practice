class Solution:
    #blocks = "WBBWWBBWBW", k = 7
    # blocks = "WBWBBBW", k = 2
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r, re = 0, 0, 0
        n = len(blocks)
        minre = n + 1
        while r < n:
            re += 1 if blocks[r] == 'W' else 0
            wlen = r - l + 1
            if wlen == k:
                minre = minre if minre < re else re
                re -= 1 if blocks[l] == 'W' else 0
                l += 1
            r += 1
        return minre
    

    def minimumRecolorsApproachII(self, blocks: str, k: int) -> int:
        w_count, minre = 0, float('inf')
        #counting all the white colors in the first window
        for i in range(k):
            if blocks[i] == 'W':
                w_count += 1
        minre = w_count
        if minre == 0:
            return minre
        # start moving the window by one and keep removing one ele from the back
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                w_count += 1
            if blocks[i - k] == 'W':
                w_count -= 1
            
            minre = min(minre, w_count)
            if minre == 0:
                return minre
        return minre



if __name__ == '__main__':
    sol = Solution()
    #print(sol.minimumRecolors("WBWBBBW", k = 2))
    print(sol.minimumRecolorsApproachII("WBBWWBBWBW", k = 7))