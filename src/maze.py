def find_path(grid, start, goal):
    """
    Return a list of (r,c) from start to end inclusive, or None if no path.
    grid contains 0 (open) and 1 (wall). Moves: up/down/left/right.
    """
    rows, cols = len(grid), len(grid[0])
    sx, sy = start
    gx, gy = goal

    # Validate start and goal coordinates
    if not (0 <= sx < rows and 0 <= sy < cols):
        return None
    if not (0 <= gx < rows and 0 <= gy < cols):
        return None

    # Check if start or goal positions are walls
    if grid[sx][sy] == 1 or grid[gx][gy] == 1:
        return None

    visited = set()

    def backtrack(r, c):
        # Check boundaries and if cell is blocked or visited
        if not (0 <= r < rows and 0 <= c < cols):
            return None
        if grid[r][c] == 1 or (r, c) in visited:
            return None

        # Check if goal reached
        if (r, c) == goal:
            return [(r, c)]

        visited.add((r, c))

        # Explore neighbors: up, down, left, right
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            path = backtrack(r + dr, c + dc)
            if path is not None:
                return [(r, c)] + path

        # Backtrack if no path found here
        return None

    return backtrack(sx, sy)
