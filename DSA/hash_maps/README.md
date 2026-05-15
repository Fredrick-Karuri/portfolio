# Data Structure: Hash Maps & Sets

A hashmap stores `key → value` pairs with O(1) average lookup, insert, and delete.
A hashset is the same idea with no values — just membership tracking.

Think: *Trade memory for speed. Turn an O(n) search into an O(1) lookup.*

---

## When to Think Hashmap / Hashset

- You're scanning an array/string and need to **remember what you've seen**
- You need to **count frequencies** of elements
- You need to **group** elements by some property
- You're looking for **pairs, complements, or duplicates**
- You want to avoid a nested loop (O(n²) → O(n))

Key insight: Hashmaps rarely *are* the data structure of the problem — they're
the **companion** that makes another structure or algorithm fast.

---

## Core Variants

### Hashset — membership only
```python
seen = set()
seen.add(x)
x in seen  # O(1)
```
Use when you only care about **whether** you've seen something.

### Hashmap — key → value
```python
count = {}
count[x] = count.get(x, 0) + 1
```
Use when you need to **store something about** what you've seen (count, index, group).

### OrderedDict — hashmap with insertion order
```python
from collections import OrderedDict
cache = OrderedDict()
cache.move_to_end(key)
cache.popitem(last=False)
```
Use when order of insertion/access matters (LRU cache, sliding window tracking).

### Counter — frequency map shortcut
```python
from collections import Counter
freq = Counter(arr)  # {element: count}
```
Use for anagram checks, frequency problems, top-k elements.

---

## Patterns in This Folder

| Pattern | When |
|---------|------|
| `seen_before/` | Detect duplicates, pairs, visited nodes |

> Most hashmap usage lives *inside* other folders — sliding window, frequency
> counting, graphs, LRU cache — because the hashmap is the tool, not the problem.
> Files land here only when the hashmap/set **is** the core insight.

---

## Key Techniques

**Complement lookup**: Store what you *need*, check if current element satisfies it (Two Sum)

**Frequency map**: `Counter(arr)` → compare, sort, filter by count

**Index map**: Store `value → index` to compute distances or ranges

**Seen set**: O(1) duplicate/cycle/visited detection

---

## Pitfalls

- **Hash collisions**: Rare in Python but know they make worst case O(n)
- **Mutable keys**: Lists and dicts can't be hashmap keys — use tuples
- **Default values**: Use `dict.get(key, default)` or `defaultdict` to avoid KeyError
- **Modifying while iterating**: Never mutate a dict/set inside a loop over it