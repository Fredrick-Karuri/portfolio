# Pattern: Breadth-First Search (BFS)

BFS explores nodes **level by level** using a queue — nearest neighbors first, then their neighbors.

Think: *Ripple outward. Closest first, always.*

---

## When to Use BFS

- **Shortest path** in an unweighted graph or grid
- **Level-order** processing (trees, grids)
- **Minimum steps** to reach a target
- When DFS would go too deep before finding the answer

Key insight: BFS guarantees the shortest path in unweighted graphs because it exhausts all distance-k nodes before any distance-(k+1) node.

---

## Core Template (Mental Model)

```python
from collections import deque

def bfs(start, grid):
    queue = deque([start])
    visited = set([start])      # mark before enqueuing, not after dequeuing

    while queue:
        node = queue.popleft()

        for neighbor in get_neighbors(node, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

> **Mark visited before enqueuing** — not after dequeuing. Marking late causes the same node to be enqueued multiple times.

---

## Grid BFS Template

```python
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def bfs_grid(grid, start_row, start_col):
    queue = deque([(start_row, start_col)])
    grid[start_row][start_col] = "0"   # sink / mark visited in-place

    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if is_valid(nr, nc, grid) and grid[nr][nc] == "1":
                grid[nr][nc] = "0"
                queue.append((nr, nc))
```

---

## BFS vs DFS

| | BFS | DFS |
|--|-----|-----|
| Data structure | Queue | Stack / recursion |
| Guarantees shortest path | Yes | No |
| Memory | O(w) — width of graph | O(h) — height/depth |
| Best for | Shortest path, levels | Connected components, backtracking |

---

## Pitfalls

- **Marking visited after dequeue**: Same node enqueued multiple times → TLE or wrong answer
- **Not validating bounds before enqueuing**: Index out of range on grids
- **Using a list as a queue**: `list.pop(0)` is O(n) — always use `deque`

---

## Problems

| Problem | File | Key Twist |
|---------|------|-----------|
| Binary Tree Level Order Traversal (LC 102) | `binary_tree_level_order_traversal.py` | Snapshot `len(queue)` at start of each level |
| Number of Islands BFS (LC 200) | `num_islands_bfs.py` | Sink cells in-place, each BFS trigger = one island |