# Pattern: Frequency Grouping

Group or compare strings by reducing them to a **canonical key** — sorted characters or a frequency signature — then use a hashmap to bucket them.

Think: *If two strings are equivalent under some transformation, they share a key.*

---

## When to Use This Pattern

- Problem asks to **group** strings that share a property (anagrams, same character counts)
- You need to check if two strings are **equivalent** without direct comparison
- Problem involves **character frequencies** as the distinguishing feature

Key insight: Sorting a string destroys order but preserves composition. Two anagrams always sort to the same string — that sorted string is your hashmap key.

---

## Core Template (Mental Model)

```python
from collections import defaultdict

def group_by_signature(strs):
    groups = defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))   # or tuple(freq_array) for O(k) key
        groups[key].append(s)

    return list(groups.values())
```

---

## Common Variations

### Sorted string as key — O(k log k) per string
```python
key = ''.join(sorted(word))
```
Simple, readable. Fine for most interview cases.

### Frequency tuple as key — O(k) per string
```python
count = [0] * 26
for c in word:
    count[ord(c) - ord('a')] += 1
key = tuple(count)
```
Better when k is large or you need strict O(k) per word.

---

## Key Patterns

**Canonical key**: Any transformation that maps equivalent strings to the same value

**defaultdict(list)**: Cleaner than checking `if key not in map` manually

**Frequency array → tuple**: Tuples are hashable; lists are not

---

## Pitfalls

- **Using list as key**: Lists aren't hashable — convert to `tuple` first
- **Case sensitivity**: Clarify if `"Eat"` and `"eat"` are anagrams in the problem
- **Empty string edge case**: `sorted("")` returns `[]` → key is `""` — handle or confirm valid

---

## Problems

| Problem | Key Twist |
|---------|-----------|
| Group Anagrams (LC 49) | Sorted string as key |
| Valid Anagram (LC 242) | Compare two frequency maps directly |
| Find All Anagrams in String (LC 438) | Sliding window + frequency comparison |