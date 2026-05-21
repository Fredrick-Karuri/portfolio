# Pattern: Exhaustive Search (Permutation + Bitmask)

Try every possible arrangement and every possible orientation. Valid when the search space has a fixed, small upper bound.

Think: *If the input is tiny and bounded, brute force is optimal.*

---

## When to Use Exhaustive Search

- Input size is **fixed and small** (n ≤ 8 is a strong signal)
- Problem involves **arrangement + orientation** (permutations × flips)
- No greedy or DP shortcut exists — correctness requires checking all cases
- Total combinations stay under ~10 million

Key insight: O(1) with a large constant beats a complex algorithm with a small constant when n is fixed. Clarity wins.

---

## Core Template (Mental Model)

```python
from itertools import permutations

def exhaustive_search(items):
    for arrangement in permutations(items):           # n! orderings
        for mask in range(1 << len(items)):           # 2^n orientations
            oriented = [
                flip(item) if (mask >> i) & 1 else item
                for i, item in enumerate(arrangement)
            ]
            if is_valid(oriented):
                return "YES"
    return "NO"
```

> Two clean, separate concerns: **permutation** handles structure, **bitmask** handles orientation.

---

## Common Variations

### Permutation only
- No orientation — just try all orderings
- `6! = 720` combinations for 6 items

### Permutation + bitmask
- Each item has two states (flipped/not)
- `6! × 2^6 = 46,080` for 6 items — still tiny

### Bitmask DP (subset problems)
- When order doesn't matter but inclusion/exclusion does
- `2^n` subsets — fits n ≤ 20

---

## Key Patterns

**`itertools.permutations`**: C-level implementation — faster than manual recursion for small n

**Bitmask flip**: `(mask >> i) & 1` checks if bit i is set — clean way to encode binary choices per item

**Early return**: Return on first valid find — no need to collect all solutions

**Fixed bound check**: Multiply out the search space before coding. If it's under ~10M, brute force is fine.

---

## Pitfalls

- **Assuming brute force is always wrong**: For fixed small n it's often the intended solution
- **Manual recursion over itertools**: Harder to read, slower in Python for small n
- **Forgetting orientations**: Permutations alone miss the flip dimension

---

## Problems

| Problem | File | Key Twist |
|---------|------|-----------|
| Domino Pyramid | `domino_pyramid.py` | `6! × 2^6 = 46,080` — permutation + bitmask flip |