# Data Structure: Linked Lists

A linked list is a sequence of nodes where each node holds a value and a pointer to the next (and optionally previous) node.

Unlike arrays, there is no index — you navigate by following pointers.

Think: *A chain. O(1) to insert/remove at a known position, O(n) to find it.*

---

## When to Think Linked List

- Problem involves **ordered data with frequent insertions/deletions**
- You need **O(1) eviction or promotion** (caches, queues)
- Problem says "design a data structure" with ordering + fast updates
- You see the words: cache, LRU, LFU, history, undo, queue

Key insight: Arrays are fast to access but slow to reorder. Linked lists are the opposite — use them when **position changes matter more than random access**.

---

## Core Variants

### Singly Linked List
- Each node: `val`, `next`
- Traverse forward only
- Use for: stacks, simple queues

### Doubly Linked List
- Each node: `val`, `prev`, `next`
- Traverse both directions, O(1) removal with a pointer to the node
- Use for: LRU/LFU cache, browser history, undo stacks

---

## Core Template (Mental Model)

```python
class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None  # omit for singly linked
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # Sentinel head/tail eliminate edge cases
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_before_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
```

> **Sentinel nodes** (dummy head + tail) are the #1 trick — they eliminate
> all null checks on edge cases for empty list, first, and last node.

---

## Patterns in This Folder

| Pattern | When |
|---------|------|
| `hashmap_plus_linked_list/` | O(1) lookup + O(1) ordered eviction (LRU, LFU) |

---

## Key Techniques

**Two pointers (slow/fast)**: Cycle detection, find middle, kth from end

**Sentinel head/tail**: Eliminates null-check edge cases on insert/remove

**Hashmap + DLL**: When you need O(1) access *and* O(1) reordering

**Reverse in place**: Standard interview move — track `prev`, `curr`, `next`

---

## Pitfalls

- **Lost pointer**: Always save `next` before overwriting it during reversal
- **Off-by-one on kth from end**: Fast pointer moves k steps first, then both move
- **Forgetting 4-pointer update**: DLL remove touches `prev.next` and `next.prev` on both sides
- **Skipping sentinel setup**: Without dummy nodes, every operation needs an empty-list special case