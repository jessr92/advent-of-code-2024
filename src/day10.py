from coord import Coord, UP, DOWN, LEFT, RIGHT
from grid import Grid


def part_1(puzzle_input: list[str]) -> int:
    grid: Grid[int] = Grid(puzzle_input, lambda elem: int(elem))
    starting_points: list[Coord] = find_starting_points(grid)
    trailhead_counts: list[int] = [len(set(trailheads(grid, starting_point))) for starting_point in starting_points]
    return sum(trailhead_counts)


def part_2(puzzle_input: list[str]) -> int:
    grid: Grid[int] = Grid(puzzle_input, lambda elem: int(elem))
    starting_points: list[Coord] = find_starting_points(grid)
    trailhead_counts: list[int] = [len(trailheads(grid, starting_point)) for starting_point in starting_points]
    return sum(trailhead_counts)


def trailheads(grid: Grid[int], starting_point: Coord) -> list[Coord]:
    return find_trailheads(grid, starting_point, -1)


def find_trailheads(grid: Grid[int], coord: Coord, previous_height: int) -> list[Coord]:
    if not grid.inside_map(coord):
        return []  # Off grid
    current_height: int = grid.value_at(coord)
    if previous_height + 1 != current_height:
        return []  # Not a gradual increase
    if current_height == 9:
        return [coord]  # Found a trailhead
    trailhead_left: list[Coord] = find_trailheads(grid, coord.move(LEFT), current_height)
    trailhead_right: list[Coord] = find_trailheads(grid, coord.move(RIGHT), current_height)
    trailhead_up: list[Coord] = find_trailheads(grid, coord.move(UP), current_height)
    trailhead_down: list[Coord] = find_trailheads(grid, coord.move(DOWN), current_height)
    return trailhead_left + trailhead_right + trailhead_up + trailhead_down


def find_starting_points(grid: Grid[int]) -> list[Coord]:
    starting_points: list[Coord] = []
    for x in range(grid.max_x):
        for y in range(grid.max_y):
            coord: Coord = Coord(x, y)
            if grid.value_at(coord) == 0:
                starting_points.append(coord)
    return starting_points
