"""
Merge Sort — implemented from scratch.

Time complexity: O(n log n)
  - log(n) levels of splitting (the list is halved each time)
  - O(n) work merging at every level
"""


def merge_sort(arr):
    """Recursively split the list in half until each piece is a single
    element, then merge those pieces back together in sorted order."""
    if len(arr) <= 1:
        return arr  # base case: a single element is already "sorted"

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    """Merge two already-sorted lists into one sorted list."""
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append whatever is left over on either side
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    numbers = [8, 3, 7, 1, 9, 4, 2]
    print("Before:", numbers)
    print("After: ", merge_sort(numbers))
