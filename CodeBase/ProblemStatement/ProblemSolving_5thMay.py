class Practice5thMay:

    def second_high_and_small(self, n, a):
        smax, max = -1, -1
        smin, min = 10 ** 5 + 1, 10 ** 5 + 1

        for i in range(n):
            if a[i] > max:
                smax = max
                max = a[i]
            elif a[i] > smax and a[i] != max:
                smax = a[i]
            if a[i] < min:
                smin = min
                min = a[i]
            elif a[i] < smin and a[i] != min:
                smin = a[i]
        return [smax, smin]

    def twoSum(self, arr, target, n):
        dic = {}
        result = []
        for i in range(n):
            ele = arr[i]
            k = target - ele
            if k in dic and dic[k] == 0:
                result.append([ele, k])
                dic[ele] = 1
            else:
                dic[ele] = 0
        if len(arr) == 0:
            result.append([-1, -1])
        return result

        # if len(arr)<=1:
        #     result.append([-1, -1])
        # for i in range(0, n):
        #     ele = arr[i]
        #     if ele in dic and dic[ele] != i:
        #         result.append([arr[dic[ele]], ele])
        #     else:
        #         dic[target-ele] = i
        # return result


prc = Practice5thMay()
arr = [4, 2, 3, 4, 2, 1, 6, 5]
n = len(arr)
#print(prc.second_high_and_small(n , arr))


if __name__ == '__main__':
    obj = Practice5thMay()
    def takeInput():

        n, tar = map(int, input().strip().split(" "))
        arr = list(map(int, input().strip().split(" ")))
        return n, tar, arr


    def printAns(ans):
        for i in ans:
            if i[0] < i[1]:
                print('{} {}'.format(i[0], i[1]))
            else:
                print('{} {}'.format(i[1], i[0]))


    t = int(input().strip())
    for i in range(t):
        n, target, arr = takeInput()

        ans = obj.twoSum(arr, target, n)
        printAns(ans)



def twoSum(arr, target, n):
    dic = {}
    result = []
    for i in range(n):
        ele = arr[i]
        k = target - ele
        if k in dic and dic[k] == 0:
            result.append([ele, k])
            dic[ele] = 1
        else:
            dic[ele] = 0
    if len(arr) == 0:
        result.append([-1, -1])
    return result