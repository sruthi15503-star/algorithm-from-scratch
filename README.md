# Algorithms From Scratch

A small collection of classic algorithms implemented in Python, from first principles — no libraries, no shortcuts. Each one is written to be read and understood line by line, not just run.

## Why this repo exists

Understanding *why* an algorithm works — not just being able to call it from a library — is the whole point here. Every implementation below was built by working through the underlying logic by hand first (tracing through examples, understanding the time complexity), then translating that understanding into code.

## Algorithms

### `merge_sort.py`
A divide-and-conquer sorting algorithm.
- **Time complexity:** O(n log n)
- **Approach:** recursively split the list in half until every piece is a single element, then merge sorted halves back together, always taking the smaller "front" element from either side.

### `binary_search.py`
An efficient search algorithm for sorted data.
- **Time complexity:** O(log n)
- **Requirement:** the input list must already be sorted.
- **Approach:** repeatedly check the middle element and discard the half of the list that can't contain the target, halving the search space every step.

## How to run

Each file can be run directly and includes a small built-in example:

```bash
python merge_sort.py
python binary_search.py
```

## What's next

More algorithms (dynamic programming, greedy algorithms, k-NN) will be added here as this collection grows.
