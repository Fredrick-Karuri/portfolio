# Data Structure: Graphs

A graph is a set of nodes (vertices) connected by edges. Unlike trees, graphs can have cycles, disconnected components, and edges in any direction.

Think: *Nodes and relationships. Everything is reachable — or isn't.*

---

## When to Think Graph

- Problem involves **connections, dependencies, or relationships**
- Data has **no clear hierarchy** (unlike trees)
- Keywords: islands, regions, paths, cycles, connected components, prerequisites

Key insight: Many problems that don't look like graphs are graphs — grids are graphs where each cell connects to its 4 neighbors.

---

## Core Variants

### Undirected
- Edges go both ways
- Used for: islands, connected components, friendship networks

### Directed (Digraph)
- Edges have direction
- Used for: prerequisites, dependency resolution, cycle detection

### Weighted
- Edges have costs
- Used for: shortest path (Dijkstra, Bellman-Ford)

---

## Representations

```python
# Adjacency list — most common in interviews
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

# Grid as implicit graph
directions = [(-1,0), (1,0), (0,-1), (0,1)]
neighbors = [(r+dr, c+dc) for dr, dc in directions]
```

---

## Traversal Choice

| Use | When |
|-----|------|
| BFS | Shortest path, level-by-level, minimum steps |
| DFS | Connected components, cycle detection, backtracking |

---

## Patterns in This Folder

| Pattern | When |
|---------|------|
| `dfs/` | Islands, components, cycle detection, flow problems |
| `bfs/` | Shortest path, level traversal, minimum steps on grids |
| `backtracking/` | Exhaustive search on graph structure (word search, combinations) |

---

## Key Techniques

**Visited set**: Always track visited nodes — graphs have cycles, trees don't

**Sink in-place**: For grid problems, overwrite visited cells instead of a separate set

**Topological sort**: For directed acyclic graphs with dependencies — use BFS (Kahn's) or DFS

---

## Pitfalls

- **Forgetting visited tracking**: Infinite loop on any cycle
- **Marking visited too late**: Mark before enqueuing/pushing, not after processing
- **Assuming connected**: Always handle disconnected graphs with an outer loop over all nodes
- **Grid bounds**: Validate row and col before accessing `grid[r][c]`