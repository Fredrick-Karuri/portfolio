# Reference: Sets

Unordered, mutable, no duplicates. O(1) average lookup, insert, delete.

---

## Create

```python
s = set()
s = {1, 2, 3}
s = set(arr)        # from list — deduplicates
s = set("hello")    # {'h', 'e', 'l', 'o'}
```

## Modify

```python
s.add(x)            # O(1)
s.remove(x)         # O(1) — raises KeyError if missing
s.discard(x)        # O(1) — safe, no error if missing
s.pop()             # remove arbitrary element
s.clear()
```

## Query

```python
x in s              # O(1) ← main reason to use a set
len(s)              # O(1)
```

## Set Operations

```python
a | b               # union
a & b               # intersection
a - b               # difference (in a but not b)
a ^ b               # symmetric difference (in one but not both)
a.issubset(b)
a.issuperset(b)
a.isdisjoint(b)     # True if no common elements
```

## Common Patterns

```python
# Duplicate detection
seen = set()
for x in arr:
    if x in seen:
        return x    # duplicate found
    seen.add(x)

# Deduplicate list (order not preserved)
unique = list(set(arr))

# Fast membership over static data
valid = {"YES", "NO", "MAYBE"}
if response in valid:
    pass
```

## Pitfall

```python
# Sets are unordered — no indexing
s[0]   # TypeError

# Lists and dicts can't be set elements — use tuples
s.add([1, 2])      # TypeError
s.add((1, 2))      # OK
```