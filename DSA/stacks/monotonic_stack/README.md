# Pattern: Monotonic Stack

A stack that maintains elements in strictly increasing or decreasing order.
When a new element violates the order, pop until it doesn't — each pop is an answer.

Think: *The moment something breaks the order is exactly when you have information.*

---

## When to Use This Pattern

- Problem asks for **next greater / next smaller** element
- Problem asks for **days until**, **distance to**, or **span of** something
- You need O(n) over what would be an O(n²) scan
- You see: temperatures, prices, buildings, histogram bars

Key insight: Each element is pushed and popped at most once → O(n) total.

---

## Core Template (Mental Model)

```python
def monotonic_stack(nums):
    result = [0] * len(nums)
    stack = []  # stores indices, not values

    for i, val in enumerate(nums):
        # Pop while current element breaks the monotonic property
        while stack and nums[stack[-1]] < val:  # swap < for > if decreasing
            idx = stack.pop()
            result[idx] = i - idx  # or nums[i], depending on problem
        stack.append(i)

    return result
```

> Always push **indices**, not values — you almost always need the position to compute distance or span.

---

## Common Variations

### Next Greater Element — decreasing stack
- Pop when current > top → top's next greater is current
- Remaining in stack after loop → no greater element exists (result stays 0 or -1)

### Next Smaller Element — increasing stack
- Pop when current < top → same logic, flipped condition

### Daily Temperatures (days to wait)
- `result[popped_idx] = current_day - popped_idx`

### Largest Rectangle in Histogram
- Pop when current bar is shorter than top
- Width = distance between new top and current index

---

## Key Patterns

**Decreasing stack → finds next greater**: Maintain stack where top is always the largest waiting

**Increasing stack → finds next smaller**: Maintain stack where top is always the smallest waiting

**Push index, compute on pop**: The pop moment is the answer moment

**Leftover stack**: Elements remaining after the loop never found their answer — handle as 0, -1, or the boundary

---

## Pitfalls

- **Pushing values instead of indices**: You lose position info needed for distance/span
- **Wrong comparison direction**: Decreasing stack pops on `<`, increasing stack pops on `>`
- **Forgetting leftover stack**: Elements that never get popped need a default result
- **Off-by-one on span**: Width in histogram problems is `i - stack[-1] - 1` after popping

---

## Problems

| Problem | Stack type | What gets popped |
|---------|------------|-----------------|
| Daily Temperatures (LC 739) | Decreasing | Days to next warmer temp |
| Next Greater Element I (LC 496) | Decreasing | Next greater value |
| Largest Rectangle in Histogram (LC 84) | Increasing | Max width at that height |
| Car Fleet (LC 853) | Decreasing | Faster cars caught by slower |