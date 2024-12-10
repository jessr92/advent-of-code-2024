from coord import Coord, UP, DOWN, LEFT, RIGHT


def part_1(puzzle_input: list[str]) -> int:
    grid = parse_map_to_grid(puzzle_input)
    starting_points: list[Coord] = find_starting_points(grid)
    trailhead_counts: list[int] = [len(set(trailheads(grid, starting_point))) for starting_point in starting_points]
    return sum(trailhead_counts)


def part_2(puzzle_input: list[str]) -> int:
    grid = parse_map_to_grid(puzzle_input)
    starting_points: list[Coord] = find_starting_points(grid)
    trailhead_counts: list[int] = [len(trailheads(grid, starting_point)) for starting_point in starting_points]
    return sum(trailhead_counts)


def trailheads(grid: list[list[int]], starting_point: Coord) -> list[Coord]:
    return find_trailheads(grid, starting_point, -1)


def find_trailheads(grid: list[list[int]], coord: Coord, previous_height: int) -> list[Coord]:
    if coord.x < 0 or coord.y < 0 or coord.x == len(grid[0]) or coord.y == len(grid):
        return []  # Off grid
    current_height: int = grid[coord.y][coord.x]
    if previous_height + 1 != current_height:
        return []  # Not a gradual increase
    if current_height == 9:
        return [coord]  # Found a trailhead
    trailhead_left: list[Coord] = find_trailheads(grid, coord.move(LEFT), current_height)
    trailhead_right: list[Coord] = find_trailheads(grid, coord.move(RIGHT), current_height)
    trailhead_up: list[Coord] = find_trailheads(grid, coord.move(UP), current_height)
    trailhead_down: list[Coord] = find_trailheads(grid, coord.move(DOWN), current_height)
    return trailhead_left + trailhead_right + trailhead_up + trailhead_down


def find_starting_points(grid: list[list[int]]) -> list[Coord]:
    starting_points: list[Coord] = []
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == 0:
                starting_points.append(Coord(x, y))
    return starting_points


def parse_map_to_grid(puzzle_input):
    grid: list[list[int]] = []
    for map_line in puzzle_input:
        grid.append([])
        for height in map_line:
            grid[-1].append(int(height))
    return grid
