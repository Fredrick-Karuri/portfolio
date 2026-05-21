# Data Structure: Stacks

A stack is LIFO — last in, first out. You only ever touch the top.

Think: *Undo history. The most recent thing is always the first to be resolved.*

---

## When to Think Stack

- Problem involves **matching or nesting** (parentheses, brackets, tags)
- You need to **defer a decision** until you see what comes next
- Problem asks for **next greater/smaller** in a sequence
- You're doing DFS **iteratively**

Key insight: Stacks shine when the answer to an earlier element depends on a later element — you hold it in the stack until that later element arrives.

---

## Core Variants

### Plain Stack — LIFO processing
```python
stack = []
stack.append(x)   # push
stack.pop()       # pop
stack[-1]         # peek
```

### Monotonic Stack — ordered stack
- Maintains increasing or decreasing order
- Pop when order is violated — each pop is an answer
- O(n) solution to what would be O(n²) nested scanning

---

## Patterns in This Folder

| Pattern | When |
|---------|------|
| `monotonic_stack/` | Next greater/smaller, spans, histogram, temperatures |

---

## Key Techniques

**Push indices, not values**: Almost always need position for distance/span computation

**The pop moment is the answer moment**: Violation of monotonic property = information

**Leftover = unanswered**: Elements still in stack after the loop never found their match

---

## Pitfalls

- **Wrong comparison**: Decreasing stack pops on `<`; increasing stack pops on `>`
- **Using values instead of indices**: Lose position info needed for span/distance
- **Forgetting to handle remaining stack**: Default result for unpopped elements