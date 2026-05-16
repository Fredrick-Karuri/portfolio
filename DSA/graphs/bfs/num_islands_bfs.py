from collections import deque

class Solution:
    """
    THE PROBLEM: count the total number of distinct Islands in a 2D graph

    PATTERN: Graph / Breadth-First-Searc (BFS) matrix Traversal

    INSIGHT: Treat each '1' as a starting node. When you find a '1',
    use BFS to visit and mark all connected land neighbours (1's)
    as water (0's ) so they are not counted again. Each complete BFS signals one Island

    THE PLAN:
    1. Guard check: Return 0 if the grid is empty
    2. Initialize an island count variable to 0
    3. Loop through every cell (row_index, col_index) using nested loops
    4. If grid cell is "1", increment island count and trigger a BFS
    5. In BFS: use a queue starting at (row_index, col_index), flip visited cells to 0,
    and explore adjacent neighbours (up, down, left,right)
    6. Return the total Island count

    Example: Grid with 3 isolated land clusters
    - Find first "1" at (0,0) -> BFS clears connected land -> islands = 1
    - Find next "1" at (2,2) -> BFS clears cell -> islands = 2
    - Find next "1" at (3,3) -> BFS clears connected land -> islands = 3
    Result: 3

    TIME: O(m * n) - Every cell is visited at most a constant number of times
    SPACE: O(min(m * n)) - Maximum queue size is bounded by the grid's smaller dimension

    """
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        total_rows = len(grid)
        total_columns = len(grid[0])
        island_count = 0

        for row_index in range(total_rows):
            for col_index in range(total_columns):
                if grid[row_index][col_index] == "1":
                    island_count += 1
                
                    # Start BFS to sink the discoverd Island
                    bfs_queue = deque([(row_index, col_index)])
                    grid[row_index][col_index] = "0" # Sink the current cell instantly

                    while bfs_queue:
                        current_row, current_col = bfs_queue.popleft()

                        # Define steps for up,down,left,right movements
                        directions = [(-1,0),(1,0),(0,-1),(0,1)]
                        for row_offset, col_offset in directions:
                            neighbour_row = current_row + row_offset
                            neighbour_col = current_col + col_offset
                        
                            # Validate if neighbour is within grid bounds as is unvisited land
                            is_valid_row = 0 <= neighbour_row < total_rows
                            is_valid_col = 0 <= neighbour_col < total_columns

                            if is_valid_row and is_valid_col and grid[neighbour_row][neighbour_col] =="1":
                                bfs_queue.append((neighbour_row,neighbour_col))
                                grid[neighbour_row][neighbour_col] = "0" # Sink cell before queueing
        return island_count