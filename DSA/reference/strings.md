# Reference: Strings

Ordered, **immutable** sequence of characters. Build results in a list and `join` at the end.

---

## Create

```python
s = ""
s = "hello"
s = str(n)              # int to string
s = ''.join(arr)        # list of chars to string
s = ' '.join(words)     # list of words to string
```

## Access

```python
s[0]        # O(1)
s[-1]       # O(1)
s[1:4]      # slice — O(k)
s[::-1]     # reversed copy — O(n)
```

## Query

```python
len(s)
x in s                  # O(n)
s.index(x)              # O(n) — raises ValueError if missing
s.count(x)              # O(n)
s.find(x)               # O(n) — returns -1 if missing
```

## Transform

```python
s.lower() / s.upper()
s.strip()               # remove leading/trailing whitespace
s.lstrip("0")           # strip leading zeros
s.replace(old, new)
s.split()               # split on whitespace
s.split(',')            # split on delimiter
```

## Check

```python
s.isalpha()             # all letters
s.isdigit()             # all digits
s.isalnum()             # letters and digits
s.startswith(prefix)
s.endswith(suffix)
any(c.isalpha() for c in s)   # contains at least one letter
```

## Common Patterns

```python
# Frequency map
from collections import Counter
freq = Counter(s)

# Sort characters (anagram key)
key = ''.join(sorted(s))

# Palindrome check (two pointers)
left, right = 0, len(s) - 1
while left < right:
    if s[left] != s[right]:
        return False
    left += 1
    right -= 1

# Build string efficiently
result = []
result.append(char)
return ''.join(result)

# Multi-delimiter split
import re
parts = re.split(r'[.?!]', s)
```

## Pitfall

```python
# Strings are immutable — this is O(n²)
s += char       # creates new string each time

# Do this instead — O(n)
parts = []
parts.append(char)
s = ''.join(parts)
```