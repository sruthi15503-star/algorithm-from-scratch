"""
Binary Search — implemented from scratch.

Requires the input list to already be sorted.
Time complexity: O(log n) — each comparison eliminates half
the remaining search space.
"""


def binary_search(arr, target):
    """Return the index of target in arr, or -1 if not found."""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    sorted_numbers = [1, 2, 3, 4, 7, 8, 9]

    print("Searching for 7:", binary_search(sorted_numbers, 7))
    print("Searching for 5:", binary_search(sorted_numbers, 5))
