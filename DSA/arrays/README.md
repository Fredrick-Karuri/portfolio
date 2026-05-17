# Data Structure: Arrays

An array stores elements in contiguous memory, giving O(1) index access and O(n) search.

Think: *The default data structure. Most problems start here.*

---

## When to Think Array

- Input is a **list of numbers or characters**
- Problem involves **indices, positions, or ranges**
- You need to scan, compare, or aggregate elements
- Grid/matrix problems — 2D arrays

---

## Patterns in This Folder

| Pattern | When |
|---------|------|
| `binary_search/` | Sorted data, find target or boundary in O(log n) |
| `two_pointers/` | Pairs, triplets, palindromes, converging from both ends |
| `greedy/` | Maximize/minimize with a locally optimal one-pass decision |
| `prefix_suffix/` | Each answer depends on products or sums of all other elements |
| `frequency_counting/` | Top-k, majority element, count-based problems |
| `backtracking/` | Generate all subsets, combinations, or permutations |
| `matrix/` | 2D traversal, rotation, spiral order |

---

## Pattern Decision Guide

| You see... | Go to... |
|------------|----------|
| Sorted array, find value or boundary | `binary_search/` |
| Pairs or triplets summing to target | `two_pointers/` |
| Merge intervals, max profit, jump reach | `greedy/` |
| Product of all except self, range sums | `prefix_suffix/` |
| Top k frequent, majority element | `frequency_counting/` |
| All subsets or combinations | `backtracking/` |
| Rotate matrix, spiral traversal | `matrix/` |

---

## Core Operations

```python
arr = [1, 2, 3, 4, 5]

arr[i]              # O(1) access
arr.append(x)       # O(1) amortised
arr.pop()           # O(1) from end
arr.insert(i, x)    # O(n) — shifts elements
arr.pop(i)          # O(n) — shifts elements
arr.sort()          # O(n log n)
arr[::-1]           # O(n) reverse
```

---

## Key Techniques

**Sort first**: Unlocks binary search, two pointers, greedy — cheap O(n log n) investment

**Running variable**: Carry a single value (max, min, sum) instead of recomputing

**In-place modification**: Swap elements rather than creating new arrays when space matters

**Sentinel values**: `float('inf')` or `float('-inf')` to simplify min/max comparisons

---

## Pitfalls

- **Index out of bounds**: Always validate before accessing `arr[i]`
- **Modifying while iterating**: Never mutate an array inside a loop over it
- **Assuming sorted**: Confirm before applying binary search or two pointers
- **Off-by-one**: `range(n)` vs `range(n+1)`, `left < right` vs `left <= right`