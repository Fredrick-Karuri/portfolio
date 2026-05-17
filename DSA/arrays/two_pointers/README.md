# Pattern: Two Pointers

Two pointers uses multiple pointers to traverse data structures efficiently, often reducing time complexity from O(n²) to O(n).

Works when you can make decisions based on values at pointer positions.

Think: *Strategic pointer movement to explore solution space.*

---

## When to Use Two Pointers

Use two pointers when:
- Array/string is **sorted** (or can be sorted)
- Looking for **pairs/triplets** with certain properties
- Need to **compare elements** at different positions
- **Optimizing brute force** nested loops
- Processing from **both ends** or **same direction**

Common keywords: "pair", "triplet", "subarray", "palindrome", "container"

---

## Core Mental Model

Two main approaches:

> **Opposite direction**: Start at both ends, move toward each other
>
> **Same direction**: Both start at beginning, move at different speeds

```python
# Opposite direction
left, right = 0, len(arr) - 1
while left < right:
    if condition:
        left += 1
    else:
        right -= 1

# Same direction (fast/slow)
slow = 0
for fast in range(len(arr)):
    if condition:
        nums[slow], nums[fast] = nums[fast], nums[slow]
        slow += 1
```

---

## Common Variations

### Opposite Direction (Squeeze)
- Start at both ends, move based on comparison
- Examples: two sum (sorted), container with most water, valid palindrome

### Same Direction (Fast/Slow)
- Fast pointer explores, slow pointer tracks valid position
- Slow marks where the next "good" element goes — fast finds it
- Examples: remove duplicates, move zeroes, partition array

### Three Pointers
- Fix one element in outer loop, two pointers on the remaining subarray
- Always sort first — enables greedy pointer movement and duplicate skipping
- Example: three sum

### Sliding Window
- Expand window with right pointer, shrink with left when constraint violated
- Examples: longest substring, minimum window

---

## Key Patterns

**Greedy movement**: Move the pointer that can't improve the solution

**Sort first**: Required for opposite-direction and triplet problems

**Duplicate skipping**: After finding a result, advance past all equal elements before continuing

**Invariant maintenance**: Keep a property true as pointers move (e.g., slow always points to last valid position)

---

## Pitfalls

- **Infinite loops**: Ensure pointers always move each iteration
- **Off-by-one**: Use `left < right` vs `left <= right` carefully
- **Not sorted**: Many two-pointer problems require sorted input first
- **Duplicate triplets**: Skip duplicates on all three pointers in three sum

---

## Two Pointers vs Other Patterns

Use **two pointers** when: can make greedy decisions, linear scan suffices

Use **binary search** when: need O(log n), searching a specific value

Use **sliding window** when: need contiguous subarray/substring with a constraint

---

## Problems

| Problem | Variant | Key Twist |
|---------|---------|-----------|
| Container With Most Water (LC 11) | Opposite | Move shorter side |
| Three Sum Closest (LC 16) | Opposite + fix | Track closest sum |
| Three Sum (LC 15) | Three pointers | Sort + skip duplicates on all three |
| Remove Duplicates (LC 26) | Fast/slow | Slow = last unique position |
| Move Zeroes (LC 283) | Fast/slow | Swap non-zeros forward |