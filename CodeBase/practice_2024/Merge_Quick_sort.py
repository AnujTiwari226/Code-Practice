def merge_sort(arr, low, high):
    if low < high:

        mid = low + high // 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        return merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    right = mid + 1
    temp = []
    while low <= mid and right <= high:
        if arr[low] > arr[right]:
            temp.append(arr[low])
            low += 1
        else:
            temp.append(arr[right])
            right += 1
    while low <= mid:
        temp.append(arr[low])
        low += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    return temp


if __name__ == '__main__':
    mlist = [3, 4, 2, 1, 5, 7, 9, 8, 0]
    print(merge_sort(mlist, 0, len(mlist)))

