"""
Linear Search — implemented from scratch.

Works on ANY list, sorted or not — checks every element in order.
Time complexity: O(n)
"""


def linear_search(arr, target):
    """Return the index of target in arr, or -1 if not found."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    numbers = [7, 2, 9, 4, 1, 8]

    print("Searching for 4:", linear_search(numbers, 4))
    print("Searching for 100:", linear_search(numbers, 100))
