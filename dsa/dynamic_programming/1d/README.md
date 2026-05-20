# Dynamic Programming — 1D

1D Dynamic Programming is used when the state of the problem
depends on **a single variable**, and each answer can be built
from **smaller values of that same variable**.

Think of it as:
> "I'm moving forward one step at a time, reusing what I already solved."

---

## When a Problem Is 1D DP

A problem is **1D DP** if:

- The state can be written as `dp[i]`
- `i` usually represents:
  - an index
  - an amount
  - a step
  - a position in a string or array
- `dp[i]` depends only on `dp[j]` where `j < i`

If you only need **one number to describe progress**, it's 1D DP.

---

## Common 1D DP Questions

Look for phrases like:
- "minimum cost"
- "maximum profit"
- "fewest steps"
- "how many ways"
- "can we reach…"

And the answer grows as `i` increases.

---

## Core 1D DP Template

```python
dp = [inf] * (n + 1)
dp[0] = base_case

for i in range(1, n + 1):
    for each possible move:
        dp[i] = best(dp[i], dp[i - move] + cost)
```

---

## Space Optimisation

When `dp[i]` only depends on the last 1–2 values, ditch the array:

```python
# Fibonacci-style (2 variables)
prev, curr = base_0, base_1
for _ in range(2, n + 1):
    prev, curr = curr, prev + curr
```

---

## Problems

| Problem | File | Key Twist |
|---------|------|-----------|
| Climb Stairs (LC 70) | `climb_stairs.py` | Fibonacci pattern, O(1) space with two variables |
| Coin Change (LC 322) | `coin_change.py` | Min coins — `dp[i] = min(dp[i], dp[i-coin] + 1)` |
| Longest Increasing Subsequence (LC 300) | `longest_increasing_subsequence.py` | `dp[i]` = LIS ending at index i |
| Word Break (LC 139) | `word_break.py` | `dp[i]` = can we reach index i via valid words |
| Maximum Subarray (LC 53) | `max_subarray.py` | Kadane's — reset when running sum goes negative |