# Pattern: Seen Before (Hashset Lookup)

Use a set to remember what you've encountered so far, turning a nested O(n²) scan into a single O(n) pass.

Think: *"Have I seen this before?" — answer in O(1).*

---

## When to Use This Pattern

- Detecting **duplicates** in an array or string
- Finding **pairs** that meet a condition (sum, difference, complement)
- Tracking **visited nodes** in graph traversal
- Detecting **cycles** in a linked list or graph

Key insight: Every time you'd write a nested loop to "check everything before this" — a set eliminates the inner loop.

---

## Core Template (Mental Model)

```python
def find_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num   # seen before — act here
        seen.add(num)
    return None
```

---

## Common Variations

### Duplicate detection
- Add to set, check membership before adding
- Return on first hit

### Complement / pair lookup
- Store what you *need*, check if current element is it
```python
# Two Sum — store complement, not the number itself
def two_sum(nums, target):
    seen = {}           # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

### Visited tracking (graphs)
- Add node to `visited` set before or after processing
- Check membership before pushing to queue/stack

### Cycle detection (linked list)
- Add each node to seen set
- If you encounter a node already in set → cycle exists

---

## Key Patterns

**Set for membership**: When you only need yes/no — `seen = set()`

**Dict for metadata**: When you need to store index, count, or value alongside — `seen = {}`

**Complement trick**: Don't store the number, store `target - number` — then a direct lookup answers the pair question

---

## Pitfalls

- **Wrong type**: Use a `set` when you only need membership; a `dict` when you need to store extra info
- **Adding before checking**: Check `if x in seen` *before* `seen.add(x)` — order matters
- **Assuming no duplicates in input**: Always clarify constraints — duplicates change the approach

---

## Problems

| Problem | Key Twist |
|---------|-----------|
| Contains Duplicate (LC 217) | Simplest form — set membership |
| Two Sum (LC 1) | Store complement in dict with index |
| Happy Number (LC 202) | Cycle detection via seen set |
| Longest Consecutive Sequence (LC 128) | Set for O(1) neighbor lookup |