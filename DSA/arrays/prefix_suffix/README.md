# Pattern: Prefix & Suffix Products (Two-Pass)

Precompute running products (or sums) from the left, then from the right, combining both passes to answer each position in O(n) without division.

Think: *Each answer = what's to my left × what's to my right. Build both sides separately.*

---

## When to Use This Pattern

- Each element's answer depends on **all other elements** in the array
- Division is **forbidden** (or input can contain zeros)
- You need O(n) time and want to avoid nested loops
- Problem involves **range products, range sums, or span-based aggregations**

Key insight: You don't need the full product at once. Left pass gives you everything left of `i`; right pass multiplies in everything right of `i`.

---

## Core Template (Mental Model)

```python
def two_pass(nums):
    n = len(nums)
    result = [1] * n

    # Left pass: result[i] = product of all elements to the LEFT
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]

    # Right pass: multiply in product of all elements to the RIGHT
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result
```

- Time: O(n) — two linear passes
- Space: O(1) extra — result array doesn't count

---

## Common Variations

### Product Except Self
- Left pass fills prefix products, right pass multiplies in suffix products
- No division, handles zeros naturally

### Prefix Sums (Range Queries)
- Precompute `prefix[i] = sum(nums[0..i])`
- Range sum `[l, r]` = `prefix[r] - prefix[l-1]` in O(1)

```python
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + nums[i]

range_sum = prefix[r + 1] - prefix[l]
```

---

## Key Patterns

**Two-pass product**: Left product in forward pass, right product in backward pass — combine in place

**Prefix sum array**: Build once, answer range queries in O(1)

**Running variable**: Don't store full prefix/suffix arrays — carry a single `left` or `right` variable

---

## Pitfalls

- **Initializing result with 0s**: Must be `[1] * n` — you're multiplying, not adding
- **Wrong pass order**: Left pass goes forward (`range(n)`), right pass goes backward (`range(n-1, -1, -1)`)
- **Off-by-one**: `result[i] = left` *before* `left *= nums[i]` — position `i` excludes `nums[i]` itself

---

## Problems

| Problem | Key Twist |
|---------|-----------|
| Product of Array Except Self (LC 238) | Classic two-pass, no division |
| Range Sum Query (LC 303) | Prefix sum, O(1) query after O(n) build |
| Subarray Sum Equals K (LC 560) | Prefix sum + hashmap for count |