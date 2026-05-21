# Pattern: Sliding Window

A window (subarray or substring) that expands and shrinks as it moves through the data, avoiding redundant recomputation.

Think: *Don't reprocess what you already know — slide, don't restart.*

---

## When to Use Sliding Window

- Problem involves a **contiguous subarray or substring**
- You need to find **max/min/longest/shortest** under a constraint
- Brute force is O(n²) — you feel one pass should be enough
- Keywords: "subarray", "substring", "window", "consecutive", "at most k"

Key insight: Every element enters the window once and leaves once → O(n).

---

## Core Mental Model

Two approaches:

> **Fixed window**: size is given (k). Slide by adding right, removing left.
>
> **Variable window**: expand right freely, shrink left when constraint breaks.

```python
# Fixed size window
current_sum = sum(nums[:k])
for i in range(k, len(nums)):
    current_sum += nums[i] - nums[i - k]   # add right, remove left

# Variable size window
left = 0
for right in range(len(nums)):
    # expand: add nums[right]
    while constraint_broken:
        # shrink: remove nums[left]
        left += 1
    # window is valid here — update result
```

---

## Common Variations

### Fixed window — known size k
- Compute initial window, then slide one step at a time
- Examples: max average subarray, contains nearby duplicate, find anagrams

### Variable window — shrink when invalid
- Expand right until constraint breaks, shrink left until valid again
- Examples: longest substring without repeating chars, minimum subarray sum, fruit into baskets

### Window + frequency map
- Use hashmap to track character/element counts in window
- Compare maps directly for anagram problems
- Examples: find all anagrams, longest repeating character replacement

---

## Key Patterns

**Fixed remove**: `nums[i - k]` — left element is always exactly k steps behind

**Shrink condition**: `while` not `if` — keep shrinking until window is valid again

**Frequency map match**: Delete key when count hits 0 — keeps map clean for direct equality check

**max_freq trick** (character replacement): Track max frequency seen — avoids recomputing on every shrink

---

## Pitfalls

- **Using `if` instead of `while` to shrink**: One shrink step may not be enough
- **Forgetting to delete zero-count keys**: Map equality checks break if stale keys remain
- **Fixed window off-by-one**: Initial window is `nums[:k]`, slide starts at index `k`
- **Returning wrong value when no answer found**: Use `float('inf')` sentinel, return 0 if unchanged

---

## Problems

| Problem | Type | Key Twist |
|---------|------|-----------|
| Max Average Subarray I (LC 643) | Fixed | Slide sum, divide at end |
| Contains Nearby Duplicate (LC 219) | Fixed | Set as window membership tracker |
| Find All Anagrams (LC 438) | Fixed | Frequency map equality |
| Longest Substring Without Repeating (LC 3) | Variable | Shrink until duplicate removed |
| Longest Repeating Character Replacement (LC 424) | Variable | `window - max_freq <= k` validity check |
| Minimum Size Subarray Sum (LC 209) | Variable | Shrink while valid, track minimum |
| Fruit Into Baskets (LC 904) | Variable | Max 2 distinct types — hashmap size constraint |