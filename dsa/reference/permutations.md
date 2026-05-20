# Reference: Permutations

A permutation is every possible **ordering** of a set of items.

| n items | n! orderings |
|---------|-------------|
| 6 | 720 |
| 8 | 40,320 |
| 10 | 3,628,800 |

Safe brute force up to n ≈ 8.

---

## Usage

```python
from itertools import permutations

items = [1, 2, 3]

# All orderings
for perm in permutations(items):
    print(perm)  # (1,2,3), (1,3,2), (2,1,3) ...

# All orderings of length r
for perm in permutations(items, 2):
    print(perm)  # (1,2), (1,3), (2,1) ...
```

## Complexity

- Time: O(n! × n) — n! permutations, each of length n
- Space: O(n) — generator yields one permutation at a time

## When to Use

- Order matters and you need to try all arrangements
- Fixed small input (n ≤ 8)
- Often paired with a bitmask to handle orientation — see `bitmask.md`

> `itertools.permutations` is C-level — always prefer it over manual recursion.