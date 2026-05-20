# Pattern: Pointer Manipulation

Rewire node pointers in-place to reverse, merge, or restructure a linked list — no extra space needed.

Think: *Save next before you sever. Move a three-pointer window through the list.*

---

## When to Use This Pattern

- Problem asks to **reverse** all or part of a linked list
- Problem asks to **merge** two sorted lists
- You need to **reorder, rotate, or partition** nodes in-place
- O(1) space is required

Key insight: You can never overwrite `curr.next` without saving it first — losing that pointer loses the rest of the list.

---

## Core Template (Mental Model)

```python
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next   # 1. save next before severing
        curr.next = prev  # 2. flip pointer backward
        prev = curr       # 3. advance prev
        curr = nxt        # 4. advance curr

    return prev           # prev is new head
```

> Three pointers: `prev`, `curr`, `nxt`. Always save `nxt` first — every time.

---

## Common Variations

### Full reversal
- `prev = None`, loop until `curr` is None, return `prev`

### Partial reversal (reverse sublist)
- Traverse to start of sublist, reverse k nodes, reconnect to rest
- Track the node before sublist starts — you'll need to reconnect it

### Merge two sorted lists
- Compare heads, attach smaller, advance that pointer
- When one list exhausts, attach the other

---

## Key Patterns

**Three-pointer window**: `prev → curr → nxt` slides forward one step at a time

**Dummy head node**: Eliminates edge cases when the head itself may change

```python
dummy = ListNode(0)
dummy.next = head
# work with dummy.next instead of head
return dummy.next
```

**Two-pointer (slow/fast)**: Find middle, detect cycle, find kth from end

---

## Pitfalls

- **Overwriting `curr.next` before saving `nxt`**: Loses the rest of the list instantly
- **Returning `curr` instead of `prev`**: Loop exits when `curr` is None — `prev` is the new head
- **Forgetting to reconnect after partial reversal**: Reversed sublist becomes a floating island

---

## Problems

| Problem | Key Twist |
|---------|-----------|
| Reverse Linked List (LC 206) | Classic three-pointer in-place reversal |
| Reverse Linked List II (LC 92) | Partial reversal — reconnect before and after |
| Merge Two Sorted Lists (LC 21) | Dummy head + compare and attach |
| Reorder List (LC 143) | Find middle + reverse second half + merge |