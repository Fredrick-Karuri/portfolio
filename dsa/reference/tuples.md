# Reference: Tuples

Ordered, **immutable**, allows duplicates. Hashable — can be used as dict keys or set elements.

---

## Create

```python
t = ()
t = (1, 2, 3)
t = (x,)            # single element — trailing comma required
t = tuple(arr)      # from list
```

## Access

```python
t[0]        # O(1)
t[-1]       # O(1)
t[1:3]      # slice — returns tuple
```

## Query

```python
len(t)
x in t          # O(n)
t.count(x)      # O(n)
t.index(x)      # O(n)
```

## Unpack

```python
a, b, c = (1, 2, 3)
first, *rest = (1, 2, 3, 4)    # rest = [2, 3, 4]
a, b = b, a                    # swap
```

## Common Patterns

```python
# Hashable key in dict or set
seen = set()
seen.add((row, col))           # coordinate tracking

# Return multiple values
def min_max(arr):
    return min(arr), max(arr)

lo, hi = min_max([3, 1, 4])

# Named tuples for readability
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x, p.y
```

## Tuple vs List

| | Tuple | List |
|--|-------|------|
| Mutable | No | Yes |
| Hashable | Yes | No |
| Use as dict key | Yes | No |
| Speed | Slightly faster | Slightly slower |