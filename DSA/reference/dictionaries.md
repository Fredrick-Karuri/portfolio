# Reference: Dictionaries

Ordered (Python 3.7+), mutable, key-value pairs. O(1) average lookup, insert, delete.

---

## Create

```python
d = {}
d = {'a': 1, 'b': 2}
d = dict(zip(keys, values))
d = {x: x**2 for x in range(5)}

from collections import defaultdict
d = defaultdict(int)    # missing keys default to 0
d = defaultdict(list)   # missing keys default to []

from collections import Counter
d = Counter(arr)        # {element: count}
```

## Access

```python
d[key]                  # O(1) — KeyError if missing
d.get(key)              # O(1) — None if missing
d.get(key, default)     # O(1) — custom default
d.setdefault(key, [])   # insert default if missing, return value
```

## Modify

```python
d[key] = value          # insert or update — O(1)
d.pop(key)              # remove and return — O(1)
d.pop(key, None)        # safe remove
del d[key]              # O(1)
d.update({'c': 3})      # merge
```

## Query

```python
key in d                # O(1)
len(d)                  # O(1)
d.keys()
d.values()
d.items()               # (key, value) pairs
```

## Common Patterns

```python
# Frequency map
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1

# Group by key
groups = defaultdict(list)
for item in arr:
    groups[key(item)].append(item)

# Invert a dict
inverted = {v: k for k, v in d.items()}

# Iterate
for key, value in d.items():
    pass

# Most common (Counter)
from collections import Counter
top_k = Counter(arr).most_common(k)
```

## OrderedDict (LRU pattern)

```python
from collections import OrderedDict
od = OrderedDict()
od.move_to_end(key)          # move to tail
od.popitem(last=False)       # remove from head
```