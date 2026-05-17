# `[ ]` Notation Cheatsheet — DSA / LeetCode

> **Core mental model:** `[ ]` always means *"give me something AT a position"* or *"give me a slice of positions."* The data structure determines what "position" means.

---

## 1. The One Rule

```
structure[key_or_index]  →  value at that key/index
```

- **List / Array** → key is an integer (position)
- **String** → key is an integer (character position)
- **Dict / HashMap** → key is anything hashable
- **2D Array** → two keys: `[row][col]`

---

## 2. Pattern: Single Index

```python
arr = [10, 20, 30, 40]

arr[0]   # → 10   (first)
arr[-1]  # → 40   (last)
arr[-2]  # → 30   (second from last)
```

**Pattern:** Negative index = count from the back. `-1` is always the last element.

```
Index:   0    1    2    3
Value:  10   20   30   40
         ↑                ↑
       arr[0]          arr[-1]
```

---

## 3. Pattern: Slicing `[start:stop:step]`

```python
arr = [0, 1, 2, 3, 4, 5]

arr[1:4]    # → [1, 2, 3]     stop is EXCLUSIVE
arr[:3]     # → [0, 1, 2]     start omitted = 0
arr[3:]     # → [3, 4, 5]     stop omitted = end
arr[::2]    # → [0, 2, 4]     every 2nd element
arr[::-1]   # → [5, 4, 3, 2, 1, 0]  reverse
```

**The Golden Rule:** `stop` index is **never included**.

```
arr[1:4]  picks positions 1, 2, 3  (stops BEFORE 4)
```

| Slice | Meaning |
|---|---|
| `[:]` | full copy |
| `[:n]` | first n elements |
| `[-n:]` | last n elements |
| `[::−1]` | reversed |
| `[i:j]` | window from i to j-1 |

---

## 4. Pattern: 2D Arrays (Grids/Matrices)

```python
grid = [
  [1, 2, 3],   # row 0
  [4, 5, 6],   # row 1
  [7, 8, 9],   # row 2
]

grid[1][2]   # → 6   (row 1, col 2)
grid[0]      # → [1, 2, 3]   (entire row 0)
```

**Mental model:** `grid[row][col]` — always row first, col second.

```
         col→  0  1  2
row 0:        [1, 2, 3]
row 1:        [4, 5, 6]   ← grid[1]
row 2:        [7, 8, 9]
                    ↑
               grid[1][2] = 6
```

Common LeetCode patterns:
```python
rows = len(grid)
cols = len(grid[0])

# Traverse all cells
for r in range(rows):
    for c in range(cols):
        val = grid[r][c]

# 4-directional neighbors
for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
    nr, nc = r+dr, c+dc
    if 0 <= nr < rows and 0 <= nc < cols:
        neighbor = grid[nr][nc]
```

---

## 5. Pattern: Dict / HashMap

```python
d = {"a": 1, "b": 2}

d["a"]            # → 1
d["c"]            # → KeyError!
d.get("c", 0)     # → 0   (safe access with default)
d["c"] = 99       # inserts or updates
```

**Common LeetCode pattern — frequency counter:**
```python
freq = {}
for ch in "hello":
    freq[ch] = freq.get(ch, 0) + 1
# freq = {'h':1, 'e':1, 'l':2, 'o':1}
```

---

## 6. Pattern: String Indexing

Strings behave exactly like read-only arrays of characters.

```python
s = "hello"

s[0]     # → 'h'
s[-1]    # → 'o'
s[1:4]   # → 'ell'
s[::-1]  # → 'olleh'
```

**Key difference from lists:** strings are immutable — you cannot do `s[0] = 'H'`. Convert to list first.

```python
chars = list(s)
chars[0] = 'H'
result = "".join(chars)   # → "Hello"
```

---

## 7. Pattern: Two-Pointer via Indices

```python
arr = [1, 2, 3, 4, 5]
left, right = 0, len(arr) - 1

while left < right:
    # arr[left] and arr[right] are your two elements
    left += 1
    right -= 1
```

The `[ ]` here is just fetching a value at a moving pointer. The pointer (`left`, `right`) is just an integer you manipulate.

---

## 8. Pattern: Sliding Window

```python
# Fixed window of size k
k = 3
arr = [2, 1, 5, 1, 3, 2]

window_sum = sum(arr[:k])          # seed the first window
for i in range(k, len(arr)):
    window_sum += arr[i]           # add incoming element
    window_sum -= arr[i - k]      # remove outgoing element
```

```
i=3:  window is arr[1:4]  →  [1, 5, 1]
      add arr[3]=1, remove arr[0]=2
```

---

## 9. Pattern: `collections.defaultdict` and `Counter`

```python
from collections import defaultdict, Counter

# defaultdict — never KeyError, auto-initialises
d = defaultdict(int)
d["x"] += 1   # safe, no need for .get()

d = defaultdict(list)
d["key"].append(1)   # auto-creates empty list

# Counter — frequency dict shortcut
c = Counter("aabbbc")
c["a"]   # → 2
c["z"]   # → 0  (no KeyError!)
```

---

## 10. Quick Reference Card

| What you write | What you get |
|---|---|
| `arr[i]` | element at index i |
| `arr[-1]` | last element |
| `arr[i:j]` | subarray from i to j-1 |
| `arr[:j]` | from start to j-1 |
| `arr[i:]` | from i to end |
| `arr[::-1]` | reversed copy |
| `arr[i:j:2]` | every 2nd from i to j-1 |
| `grid[r][c]` | cell at row r, col c |
| `d[key]` | value at key (KeyError if missing) |
| `d.get(key, default)` | safe access |
| `s[i]` | character at position i (read-only) |

---

## 11. The Trap Patterns (Common LeetCode Bugs)

```python
# ❌ Off-by-one: stop is exclusive
arr[0:3]  # gets indices 0, 1, 2  — NOT 3

# ❌ Modifying list while iterating with index
for i in range(len(arr)):
    if arr[i] == 0:
        arr.pop(i)   # shifts everything — use two-pointer instead

# ❌ Shallow copy of 2D grid
grid2 = grid[:]          # rows are still shared!
grid2 = [row[:] for row in grid]   # ✅ correct deep copy

# ❌ Index out of range
arr[len(arr)]   # last valid index is len(arr)-1

# ❌ Dict access vs .get()
d["missing"]         # KeyError
d.get("missing", 0)  # ✅ returns 0
```

---

*The notation never changes. Only the data structure behind it does.*