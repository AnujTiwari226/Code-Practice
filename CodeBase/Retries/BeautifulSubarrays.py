from typing import List

def distinctSubKOdds(arr: List[int], numOdds: int) -> int:
    count = 0
    prefix_count = {0: 1}  # Hashmap to count occurrences of odd count
    odd_count = 0

    for num in arr:
        if num % 2 == 1:
            odd_count += 1

        # Check if there's a subarray ending here with numOdds odd numbers
        diff = odd_count - numOdds
        if (odd_count - numOdds) in prefix_count:
            count += prefix_count[odd_count - numOdds]

        # Update hashmap
        if odd_count in prefix_count:
            prefix_count[odd_count] += 1
        else:
            prefix_count[odd_count] = 1

    return count

arr = [1, 2, 3, 4, 5]
k = 2
print(distinctSubKOdds(arr, k))