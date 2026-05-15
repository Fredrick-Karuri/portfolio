# Pattern: Hashmap + Doubly Linked List

Combines a hashmap and a doubly linked list to achieve **O(1) lookup AND O(1) ordered insertion/removal**.

Neither structure alone is enough — together they cover each other's weakness.

Think: *Jump anywhere instantly (hashmap), then move/remove in place (linked list).*

---

## When to Use This Pattern

Use hashmap + doubly linked list when:
- You need **O(1) access by key**
- You also need to **track order** (recency, frequency, rank)
- You need to **evict or promote** elements in O(1)
- Problem involves a **cache**, **history**, or **ordering with fast updates**

Key insight: The hashmap stores `key → node`. The linked list gives you O(1) move/remove once you have the node.

---

## Core Template (Mental Model)

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  # key → value, insertion order maintained

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)   # promote to most recent
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # evict least recent (head)
```

> `OrderedDict` in Python *is* this pattern built-in. Use it in interviews
> unless explicitly asked to implement a doubly linked list from scratch.

---

## Structure Visualized

```
head <-> [LRU node] <-> [node] <-> [MRU node] <-> tail
              ↑                          ↑
           evict here               promote here
```

Hashmap: `key → node` (O(1) jump to any node)
List: lets you move/remove that node in O(1) since you have prev/next pointers.

---

## Common Variations

### LRU Cache (Least Recently Used)
- Evict the node that was accessed **longest ago**
- Move to tail on get/put, evict from head
- Time: O(1) get and put, Space: O(capacity)

### Manual DLL (when OrderedDict is banned)
- Implement `Node` class with `prev`, `next` pointers
- Maintain explicit `head` and `tail` sentinel nodes
- Hashmap stores `key → Node` object directly

---

## Key Patterns

**Promote on access**: `move_to_end(key)` — do this in both `get` and `put`

**Evict from head**: `popitem(last=False)` — always the least recently used

**Update existing key**: move to end first, then overwrite — don't just overwrite

**Sentinel nodes**: In manual DLL, dummy head/tail eliminate edge cases on insert/remove

---

## Pitfalls

- **Forgetting to promote on `get`**: Reading a key makes it "recently used" too
- **Overwriting without promoting**: Always `move_to_end` before updating value
- **Capacity check timing**: Check *after* inserting, not before
- **Manual DLL pointer bugs**: Always update all 4 pointers (prev/next on both neighbors)

---

## Problems

| Problem | Key Twist |
|---------|-----------|
| LRU Cache (LC 146) | Classic — use `OrderedDict` |