from src.maze import find_path

def test_simple_path():
    g = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    path = find_path(g, (0,0), (2,2))
    assert path is not None
    assert path[0] == (0,0)
    assert path[-1] == (2,2)

def test_no_path_maze():
    g = [
        [0,1,0,0],
        [0,1,0,1],
        [0,1,0,1],
        [1,0,0,1],  # Block the only path by changing (3,0) to 1
    ]
    assert find_path(g, (0,0), (3,2)) is None

def test_start_blocked():
    g = [
        [1,0],
        [0,0],
    ]
    assert find_path(g, (0,0), (1,1)) is None

def test_end_blocked():
    g = [
        [0,0],
        [0,1],
    ]
    assert find_path(g, (0,0), (1,1)) is None

def test_start_out_of_bounds():
    g = [
        [0],
    ]
    assert find_path(g, (-1,0), (0,0)) is None

def test_end_out_of_bounds():
    g = [
        [0],
    ]
    assert find_path(g, (0,0), (1,0)) is None
