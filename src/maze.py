def find_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    path = []
    visited = set()

    def backtrack(r, c):
        # Check bounds and walls
        if not (0 <= r < rows and 0 <= c < cols):
            return False
        if grid[r][c] == 1 or (r, c) in visited:
            return False
        
        # Add current cell to path and visited
        path.append((r, c))
        visited.add((r, c))
        
        # Check if reached the end
        if (r, c) == end:
            return True
        
        # Explore neighbors: up, down, left, right
        if (backtrack(r-1, c) or
            backtrack(r+1, c) or
            backtrack(r, c-1) or
            backtrack(r, c+1)):
            return True
        
        # Backtrack: remove from path if no path found
        path.pop()
        return False

    if backtrack(*start):
        return path
    else:
        return None
