# Data Structure: Strings

A string is an immutable sequence of characters. Most string problems reduce to a question about substrings, character frequencies, or pattern matching.

Think: *Strings are arrays of characters — array techniques apply, plus character-specific tricks.*

---

## When to Think Strings

- Input is text — words, sentences, characters
- Problem involves **substrings, subsequences, or character counts**
- Keywords: anagram, palindrome, window, frequency, parse, match

---

## Patterns in This Folder

| Pattern | When |
|---------|------|
| `sliding_window/` | Longest/shortest substring under a constraint |
| `frequency_grouping/` | Group or compare strings by character composition |
| `expand_around_center/` | Palindrome detection — grow outward from every center |
| `regex/` | Multi-delimiter splits, pattern extraction, input cleaning |

---

## Core Operations

```python
s.split()           # split on whitespace
s.split('x')        # split on delimiter
''.join(arr)        # join list into string
sorted(s)           # sort characters — O(k log k)
s.strip()           # remove leading/trailing whitespace
s.lower() / s.upper()
s.isalpha()         # all letters
s.isalnum()         # letters and digits
any(c.isalpha() for c in s)  # contains at least one letter
```

---

## Key Techniques

**Sorted string as key**: Two strings are anagrams if `sorted(a) == sorted(b)`

**Two pointers for palindrome**: Compare `s[left]` and `s[right]`, move inward

**Character frequency map**: `Counter(s)` or `{c: s.count(c) for c in set(s)}`

**Sliding window**: Fixed or variable window tracking a constraint over characters

---

## Pitfalls

- **Immutability**: Strings can't be modified in place — build a list and `join` at the end
- **Case sensitivity**: Clarify whether `'A'` and `'a'` are the same
- **Whitespace edge cases**: `.split()` handles multiple spaces; `.split(' ')` does not
- **Empty string**: Always check `if not s` before indexing