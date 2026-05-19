# DSA — Data Structures & Algorithms

A structured collection of LeetCode solutions organised by **data structure first, pattern second**.

Think: *When you see a problem, identify the data structure → navigate to the pattern → recall the template.*

---

## How to Navigate

**Step 1 — Identify the data structure** the problem operates on.
**Step 2 — Find the pattern** (subfolder) that matches the technique.
**Step 3 — Read the README** for the mental model and template.
**Step 4 — Check the problems table** to find the closest solved example.

---

## Folder Map

```
DSA/
├── arrays/
│   ├── binary_search/       — sorted data, eliminate half each step
│   ├── two_pointers/        — converging or parallel pointers on sorted/pair problems
│   ├── greedy/              — sort + commit locally optimal choice
│   ├── prefix_suffix/       — precompute left/right products or sums
│   ├── frequency_counting/  — top-k, majority element, count-based problems
│   ├── backtracking/        — subsets, combinations, permutations
│   └── matrix/              — 2D array manipulation, rotation, traversal
│
├── strings/
│   ├── sliding_window/      — variable/fixed window over characters
│   ├── frequency_grouping/  — canonical key (sorted/freq) + hashmap bucketing
│   └── expand_around_center/— palindrome problems, grow from every center
│
├── linked_lists/
│   ├── hashmap_plus_linked_list/ — O(1) lookup + O(1) ordered eviction (LRU)
│   └── pointer_manipulation/    — reverse, merge, reorder nodes in-place
│
├── trees/
│   ├── binary_trees/        — construction, LCA, depth problems
│   ├── bst/                 — ordered property, in-order traversal tricks
│   └── bfs/                 — level-order traversal
│
├── graphs/
│   ├── dfs/                 — islands, connected components, cycle detection
│   ├── bfs/                 — shortest path, min steps on grids
│   └── backtracking/        — word search, combination sum on graph structure
│
├── dynamic_programming/
│   ├── 1d/                  — coin change, LIS, word break, climb stairs
│   ├── 2d/                  — grid paths, edit distance
│   └── knapsack/            — include/exclude decisions, subset sum
│
├── hash_maps/
│   └── seen_before/         — duplicate detection, complement lookup, visited tracking
│
├── stacks/
│   └── monotonic_stack/     — next greater/smaller, spans, temperatures
│
├── bit_manipulation/        — binary ops, XOR tricks, bit counting
│
└── reference/               — Python built-in cheatsheets (dict, list, set, string)
```

---

## Pattern Decision Guide

| You see... | Start in... |
|------------|-------------|
| Sorted array, find target | `arrays/binary_search` |
| Pairs, opposites, converging | `arrays/two_pointers` |
| Subarray / substring window | `strings/sliding_window` |
| Group / compare strings | `strings/frequency_grouping` |
| Palindrome | `strings/expand_around_center` |
| Prefix products / range sums | `arrays/prefix_suffix` |
| Min/max over intervals or tasks | `arrays/greedy` |
| Cache with ordering | `linked_lists/hashmap_plus_linked_list` |
| Reverse, merge, reorder list | `linked_lists/pointer_manipulation` |
| Tree level by level | `trees/bfs` |
| Connected components, islands | `graphs/dfs` |
| Shortest path, min steps on grid | `graphs/bfs` |
| "How many ways" / min cost | `dynamic_programming/` |
| Have I seen this before? | `hash_maps/seen_before` |
| All subsets / combinations | `arrays/backtracking` |
| Next greater/smaller element | `stacks/monotonic_stack` |
| Binary string, even/odd, XOR | `bit_manipulation/` |

---

## Principles

**Data structure first**: The folder you land in is determined by what the problem *operates on*, not just what technique it uses.

**Hashmaps are tools, not homes**: Most hashmap usage lives inside other patterns (sliding window, graphs, greedy). Files only land in `hash_maps/` when the hashmap *is* the core insight.

**READMEs are your interview flashcards**: Every pattern folder has a README with a mental model, core template, variations, and pitfalls. Read it before the problem, not after.