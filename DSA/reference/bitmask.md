# Reference: Bitmask

A bitmask uses an integer's binary representation to encode **n binary choices** simultaneously.

| n items | 2^n masks |
|---------|-----------|
| 6 | 64 |
| 8 | 256 |
| 20 | 1,048,576 |

Safe brute force up to n ≈ 8. Bitmask DP up to n ≈ 20.

---

## Usage

```python
items = ['a', 'b', 'c']
n = len(items)

# Iterate all 2^n subsets
for mask in range(1 << n):           # 1 << n == 2^n
    for i in range(n):
        if (mask >> i) & 1:          # bit i is set → item i is selected
            print(items[i])

# Flip example (paired with permutations)
dominoes = [(1, 2), (3, 4), (5, 6)]
mask = 0b101  # flip domino 0 and domino 2

oriented = [
    (b, a) if (mask >> i) & 1 else (a, b)
    for i, (a, b) in enumerate(dominoes)
]
```

## Key Operations

```python
1 << n           # 2^n — total number of masks
(mask >> i) & 1  # check if bit i is set
mask | (1 << i)  # set bit i
mask & ~(1 << i) # clear bit i
bin(mask)        # see binary representation
```

## Complexity

- Time: O(2^n × n) — 2^n masks, n bits each
- Space: O(1) — no extra storage needed

## When to Use

- Each item has exactly two states (flip/no-flip, include/exclude, on/off)
- Fixed small input — brute force (n ≤ 8) or bitmask DP (n ≤ 20)
- Often paired with permutations — see `permutations.md`