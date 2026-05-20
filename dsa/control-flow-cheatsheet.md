# Control Flow Cheatsheet — `for`, `while`, `if` for DSA / LeetCode

> **Core mental model:** `for` = you know the count. `while` = you know the condition. `if` = gate on a value.

---

## 1. `for` — When You Know the Shape

```python
for item in iterable:       # over elements directly
for i in range(n):          # over indices 0..n-1
for i, val in enumerate(arr):  # index AND value together
for a, b in zip(arr1, arr2):   # two arrays in lockstep
```

### `range` patterns

```python
range(n)        # 0, 1, 2, ..., n-1
range(1, n)     # 1, 2, ..., n-1
range(n, 0, -1) # n, n-1, ..., 1   (reverse, stop exclusive)
range(0, n, 2)  # 0, 2, 4, ...     (step 2)
```

**The rule:** `range(start, stop, step)` — stop is always **exclusive**.

```
range(2, 8, 2) → 2, 4, 6   (stops BEFORE 8)
```

### When to use `for`

| Situation | Pattern |
|---|---|
| Visit every element | `for x in arr` |
| Need the index | `for i in range(len(arr))` |
| Need index + value | `for i, x in enumerate(arr)` |
| Two-pointer (fixed step) | `for i in range(n); j = n-1-i` |
| Build prefix sums | `for i in range(1, n)` |
| Matrix traversal | nested `for r` / `for c` |

---

## 2. `while` — When You Control the Advance

```python
while condition:
    # you decide when to move forward
```

Use `while` when the loop variable moves **irregularly** — sometimes 1 step, sometimes 2, sometimes not at all.

### Core patterns

```python
# Two pointers (classic)
left, right = 0, len(arr) - 1
while left < right:
    if arr[left] + arr[right] == target:
        return [left, right]
    elif arr[left] + arr[right] < target:
        left += 1
    else:
        right -= 1

# Sliding window (variable size)
left = 0
for right in range(len(arr)):     # right always moves
    window.add(arr[right])
    while window_is_invalid:      # left catches up conditionally
        window.remove(arr[left])
        left += 1

# Binary search
lo, hi = 0, len(arr) - 1
while lo <= hi:                   # note: <= not <
    mid = (lo + hi) // 2
    if arr[mid] == target: return mid
    elif arr[mid] < target: lo = mid + 1
    else: hi = mid - 1

# BFS
from collections import deque
q = deque([start])
while q:
    node = q.popleft()
    for neighbor in graph[node]:
        q.append(neighbor)
```

### `for` vs `while` — the decision

| Signal | Use |
|---|---|
| Traversal is uniform (every index, every element) | `for` |
| Pointers move conditionally / at different speeds | `while` |
| You control when to advance | `while` |
| BFS, two pointers, binary search | `while` |
| DFS, prefix work, building results | `for` |

---

## 3. `if / elif / else` — Gate Patterns

```python
if condition:
    ...
elif other_condition:
    ...
else:
    ...
```

### In-line (ternary) — use for assignments, not logic

```python
val = x if x > 0 else 0       # ✅ simple assignment
result = a if a > b else b     # max without max()
```

### Common DSA gate patterns

```python
# Bounds check before accessing (critical in grids)
if 0 <= r < rows and 0 <= c < cols:
    process(grid[r][c])

# Early return (prune)
if not arr: return 0
if left > right: return -1   # base case in recursion

# Membership check
if key in d:          # O(1) for dict/set
if val in arr:        # O(n) for list — usually a signal to use a set

# Frequency-based gate
if freq[char] > 1:
    ...

# Cascade (order matters — most specific first)
if x < 0:   ...        # negatives
elif x == 0: ...       # zero
else:        ...       # positives
```

---

## 4. `break` and `continue` — Precision Control

```python
# break: exit the loop entirely
for i in range(n):
    if arr[i] == target:
        result = i
        break          # stop as soon as found

# continue: skip this iteration, keep going
for x in arr:
    if x % 2 == 0:
        continue       # skip even numbers
    process(x)

# else on a loop: runs only if loop completed WITHOUT break
for x in arr:
    if x == target:
        break
else:
    print("not found")   # only runs if break never hit
```

---

## 5. Nested Loops — Complexity Signal

```python
for i in range(n):          # O(n²) — brute force signal
    for j in range(n):
        ...

for i in range(n):          # O(n²) — same
    for j in range(i+1, n): # j starts after i (pairs)
        ...
```

**Pattern recognition:** if you're writing nested loops and the problem expects O(n log n) or O(n), that's the signal to switch to two pointers, binary search, or a hash map.

```python
# O(n²) brute force → O(n) with a set
for i in range(n):
    for j in range(i+1, n):           # looking for complement
        if arr[i] + arr[j] == target: # ← this nested loop

# Becomes:
seen = set()
for x in arr:
    if target - x in seen: return True
    seen.add(x)
```

---

## 6. Quick Reference Card

| Construct | Argument shape | Key rule |
|---|---|---|
| `for x in arr` | iterable | visits elements |
| `for i in range(n)` | `(stop)` | 0 to n-1 |
| `for i in range(a,b)` | `(start, stop)` | a to b-1 |
| `for i in range(a,b,s)` | `(start, stop, step)` | step can be negative |
| `enumerate(arr)` | iterable | yields `(index, value)` |
| `zip(a, b)` | two iterables | yields `(a[i], b[i])` |
| `while cond` | boolean expression | runs until False |
| `while lo <= hi` | binary search | `<=` not `<` |
| `if x in dict` | key | O(1) |
| `if x in list` | value | O(n) — use set instead |
| `break` | none | exits loop |
| `continue` | none | skips to next iteration |
| `for...else` | none | `else` runs if no `break` |

---

## 7. The Trap Patterns

```python
# ❌ Infinite while — forgot to advance
while left < right:
    if condition: left += 1
    # else: nothing — right never moves, loops forever
# ✅ Always ensure BOTH pointers can move

# ❌ Off-by-one in range
for i in range(n+1):   # goes 0..n — usually wrong
for i in range(n):     # ✅ goes 0..n-1

# ❌ Modifying a list while iterating it
for x in arr:
    if x == 0: arr.remove(x)   # skips elements silently
# ✅ Iterate a copy, or build a new list
result = [x for x in arr if x != 0]

# ❌ Binary search: wrong boundary
while lo < hi:            # misses the case lo == hi
while lo <= hi:           # ✅ correct

# ❌ Checking membership in a list inside a loop
for x in arr:
    if x in other_list:  # O(n) inside O(n) = O(n²)
other_set = set(other_list)
for x in arr:
    if x in other_set:   # ✅ O(1) lookup
```

---

*`for` knows the count. `while` knows the condition. `if` guards the gate.*