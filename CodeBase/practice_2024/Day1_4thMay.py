def pair_sum(arr:[int], s:int):
    list1 = []
    arr.sort()
    for i in range(len(arr)):
        ele = arr[i]
        for j in range(i+1, len(arr)):
            if ele + arr[j] == s:
                list1.append([ele, arr[j]])
    return list1


# print(pair_sum([4, 2, 1, 3, 4, 2, 5, 0], 5))

def get_sum_of_even_odd(n: [int]):
    nums = list(map(int, str(n)))
    even, odd = 0, 0
    for x in nums:
        if x % 2 == 0:
            even += x

    for x in nums:
        if x % 2 != 0:
            odd += x
    print(even, end=' ')
    print(odd)


n = input()
get_sum_of_even_odd(n)