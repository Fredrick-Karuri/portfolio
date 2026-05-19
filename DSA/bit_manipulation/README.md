# Data Structure: Bit Manipulation

Operating directly on binary representations — faster and more space-efficient than arithmetic equivalents.

Think: *Skip the math. Work on the bits directly.*

---

## When to Think Bit Manipulation

- Problem involves **binary strings or binary representations**
- Keywords: even/odd, power of two, single number, flip, set/clear bit
- You need O(1) space and the input is numeric or binary

Key insight: Division by 2 = right shift. Multiply by 2 = left shift. Even/odd = check last bit.

---

## Core Operations

```python
n & 1          # check if odd (last bit is 1)
n >> 1         # divide by 2 (right shift)
n << 1         # multiply by 2 (left shift)
n & (n - 1)    # clear lowest set bit
n ^ n          # XOR — cancels equal values (used for finding unique element)
```

---

## Core Template (Mental Model)

```python
# Process binary string right to left
for i in range(len(s) - 1, 0, -1):
    if s[i] == '0':
        # even — one operation (divide by 2)
    else:
        # odd — two operations (subtract 1, then divide by 2)
# handle final leading '1' separately
```

---

## Common Variations

### Binary string simulation
- Strip leading zeros, scan right to left
- Count operations per bit type

### XOR tricks
- `a ^ a = 0` — cancels duplicates
- Find the one unique number in an array of pairs: `reduce(xor, nums)`

### Power of two check
- `n > 0 and (n & (n - 1)) == 0`

### Count set bits (Hamming weight)
- `bin(n).count('1')` or loop with `n & (n-1)` to clear bits one by one

---

## Pitfalls

- **Operator precedence**: `&`, `|`, `^` have lower precedence than `==` — always use parentheses
- **Signed integers**: Right shift on negatives behaves differently — use unsigned where needed
- **Forgetting the leading bit**: In binary string problems the leftmost `'1'` often needs special handling

---

## Problems

| Problem | File | Key Twist |
|---------|------|-----------|
| Number of Steps to Reduce to Zero (LC 1342) | `num_steps_reduce_to_zero.py` | `'0'` costs 1 op, `'1'` costs 2, final leading `'1'` costs 1 |