class ProblemSolving:

    def rotateArray(self, arr: [], n: int) -> []:
        templ = [0] * n
        for i in range(1, n):
            templ[i - 1] = arr[i]
        templ[n - 1] = arr[0]
        return templ

    def rotateArrayByK(self, arr: list, k: int) -> list:
        n = len(arr)
        while k > 0:
            temp = arr[0]
            for i in range(n - 1):
                arr[i] = arr[i+1]
            arr[n-1] = temp
            k -= 1
        return arr

    def rotateArrayByK_M2(self, arr: list, k: int) -> list:
        n = len(arr)
        i = 0
        count = k
        out = 2 % 4
        while k > 0 and i < n:
            j = n + i - count
            temp = arr[0]
            arr[i] = arr[i+1]
            arr[j] = temp
            k -= 1
            i += 1
        return arr

obj = ProblemSolving()
l1 = [1, 2, 3, 4, 5]
# print(obj.rotateArray(l1, n=5))
l2 = [1, 2]
print(obj.rotateArrayByK_M2(l1, k=3))



