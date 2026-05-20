# Pattern: Expand Around Center

Every palindrome has a center. Iterate over all possible centers and expand outward while characters match — no extra space needed.

Think: *Plant a flag at every position, grow outward until it breaks.*

---

## When to Use This Pattern

- Problem involves finding or validating **palindromic substrings**
- You need O(n²) time but only **O(1) space** (vs O(n²) DP table)
- Problem asks for **longest**, **count**, or **existence** of palindromic substrings

Key insight: There are `2n - 1` possible centers (n odd-length, n-1 even-length). Check all of them.

---

## Core Template (Mental Model)

```python
def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1   # overshoot by 1 on each side

def longest_palindrome(s):
    best_start, best_end = 0, 0

    for i in range(len(s)):
        # Odd length — single center
        l, r = expand(s, i, i)
        if r - l > best_end - best_start:
            best_start, best_end = l, r

        # Even length — two centers
        l, r = expand(s, i, i + 1)
        if r - l > best_end - best_start:
            best_start, best_end = l, r

    return s[best_start:best_end + 1]
```

---

## Common Variations

### Longest palindromic substring
- Track `best_start, best_end` across all expansions
- Return `s[best_start:best_end + 1]`

### Count palindromic substrings (LC 647)
- Instead of tracking longest, increment counter on every valid expansion step

```python
count = 0
for i in range(len(s)):
    for left, right in [(i, i), (i, i + 1)]:  # odd + even
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
```

---

## Key Patterns

**Odd + even centers**: Always handle both — forgetting even centers misses palindromes like `"abba"`

**Expand returns overshot indices**: Loop exits one step too far — return `left + 1, right - 1`

**2n - 1 centers**: n single-char + (n-1) between-char gaps

---

## Pitfalls

- **Only checking odd centers**: Missing even-length palindromes like `"abba"`
- **Off-by-one on return**: Expansion stops *after* mismatch — remember to add/subtract 1
- **Mutating indices in outer loop**: Use a helper `expand()` so `i` stays clean

---

## Problems

| Problem | Key Twist |
|---------|-----------|
| Longest Palindromic Substring (LC 5) | Track best start/end across all centers |
| Palindromic Substrings (LC 647) | Count every valid expansion step |