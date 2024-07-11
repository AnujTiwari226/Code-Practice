class Sorting:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def selection_sort(self):
        print("Selection Sort")
        list1 = self.arr
        for i in range(0, self.n-1):
            mi = i
            for j in range(i, self.n):
                if list1[j] < list1[mi]:
                    list1[mi], list1[j] = list1[j], list1[mi]

        return list1

    def bubble_sort(self):
        print("Bubble Sort")
        blist = self.arr
        l = self.n
        for i in range(l - 1, 0, -1):
            m = i
            dswap = 0
            for j in range(0, m):
                if blist[j] > blist[j+1]:
                    blist[j], blist[j+1] = blist[j+1], blist[j]
                    dswap = 1
            if dswap == 0:
                break
        return blist

    def insertiion_sort(self):
        print("Insertion Sort")
        ilist = self.arr
        l = self.n
        for i in range(0, l):
            j = i
            while j > 0 and (ilist[j - 1] > ilist[j]):
                ilist[j], ilist[j-1] = ilist[j-1], ilist[j]
                j -= 1
        return ilist


myobj = Sorting([4, 8, 9, 10, 5, 6, 11, 2, 1])
# flist = myobj.bubble_sort()
# print(flist)
# slist = myobj.selection_sort()
# print(slist)
ilist = myobj.insertiion_sort()
print(ilist)
