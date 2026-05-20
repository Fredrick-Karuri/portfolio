# Reference: Lists

Ordered, mutable, allows duplicates. The default Python sequence.

---

## Create

```python
arr = []
arr = [1, 2, 3]
arr = [0] * n          # n zeros
arr = list(range(n))   # [0, 1, ..., n-1]
arr = [x for x in iterable if condition]
```

## Access

```python
arr[0]      # first — O(1)
arr[-1]     # last — O(1)
arr[1:4]    # slice [1, 2, 3] — O(k)
arr[::-1]   # reversed copy — O(n)
```

## Modify

```python
arr.append(x)        # add to end — O(1)
arr.pop()            # remove from end — O(1)
arr.insert(i, x)     # insert at index — O(n)
arr.pop(i)           # remove at index — O(n)
arr.remove(x)        # remove first occurrence — O(n)
arr[i] = x           # update at index — O(1)
```

## Query

```python
len(arr)             # O(1)
x in arr             # O(n)
arr.index(x)         # first index of x — O(n)
arr.count(x)         # O(n)
min(arr), max(arr)   # O(n)
sum(arr)             # O(n)
```

## Sort

```python
arr.sort()                        # in-place — O(n log n)
arr.sort(reverse=True)
arr.sort(key=lambda x: x[1])
sorted(arr)                       # returns new list
```

## Common Patterns

```python
# Stack (LIFO)
stack = []
stack.append(x)
stack.pop()

# Two pointers
left, right = 0, len(arr) - 1

# Enumerate
for i, val in enumerate(arr):
    pass

# Zip
for a, b in zip(arr1, arr2):
    pass

# Flatten 2D
flat = [x for row in matrix for x in row]
```